import marko
from marko.block import FencedCode

import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
import re
from numpy import sin, cos, tan, exp, log, sqrt, pi, e, sqrt
import sys


def extract_code_blocks(md_text):
    parsed = marko.parse(md_text)

    code_blocks = []

    def extract_from_node(node):
        if isinstance(node, FencedCode):
            language = node.lang if node.lang else "None"
            code_blocks.append({'language': language, 'code': node.children})
        if hasattr(node, 'children'):
            for child in node.children:
                extract_from_node(child)

    extract_from_node(parsed)

    return code_blocks


# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parser.py <path-to-markdown-file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    src2out_dir = file_path.parent
    out2asset_dir = Path("assets")
    src2asset_dir = Path(src2out_dir / out2asset_dir)

    with open(sys.argv[1], 'r') as file:
        md_content = file.read()

    blocks = extract_code_blocks(md_content)
    finds = re.findall(r"```\s*plot\n.*?\n```", md_content, re.DOTALL)

    if not blocks:
        print("No code blocks found in the markdown content")

    if not Path(src2asset_dir).exists():
        Path(src2asset_dir).mkdir()

    plots = []

    for i, (find, block) in enumerate(zip(finds, blocks)):
        if block['language'] != 'plot':
            continue
        x_min, x_max = -1, 3
        x = np.linspace(x_min, x_max, 400)
        code_lines = block['code'][0].children.split('\n')[:-1]
        for line in code_lines:
            configs = re.findall(r"(\[([a-zA-Z]+)=([a-zA-Z]+)\])", line)
            for config in configs:
                pass    # TODO: Implement configuration: colors, contours, and scatter
            line = re.sub(r'\[.*?\]', '', line)
            y = eval(line)
            plt.plot(x, y)
        name = f"plot-{i}.png"
        plt.savefig(src2asset_dir/name)
        plt.close()
        md_content = md_content.replace(find, f"![{name}]({out2asset_dir/name})")

    with open(src2out_dir / 'out.md', 'w') as file:
        file.write(md_content)
