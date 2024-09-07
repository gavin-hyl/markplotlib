# Markplotlib - `matplotlib` Integration for Markdown

## Usage

`python3 parser.py <path-to-md-file>` will replace all instances of the `plot` annotated code blocks with plots generated with `matplotlib`.

The markdown file should contain snippets such as
````markdown
```plot
[config_option=value] [config_option=value] <expression>
<expression>
[config_option=value] <expression>
```
````
where `<expression>` is an explicit expression to be plotted containing the symbol `x`. Each line in the markdown source code will be plotted separately.

For example, 

````markdown
```plot
[color=blue](x < 1) * -1 + (x >= 1) * 10 * (x - 11/10)
-x ** 3
sin(6.28 * x)
```
````

will be replaced by
```
![plot-0.png](assets\plot-0.png)
```

## Features

- automatic plot generation using `matplotlib`
- python syntax for defining plots
- customizable graph settings using configurations (size, min/max for axes, solid-dashed-scatter, etc.) - not fully implemented yet
- small pet project, enjoy😀