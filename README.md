# Python Sphinx Highlighter

This is an extension for [Visual Studio Code](https://code.visualstudio.com/) designed to improve readbility of [Python](https://www.python.org/) docstrings using the the [Sphinx docstring format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html).

## Features

![Sphinx docstring highlight comparison](images/comparison.gif)

*The source code shown is the the example from the [Read the Docs Sphinx docstring format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html#an-example-class-with-docstrings) introduction.*

Sphinx docstrings are compact and can easily be converted into HTML or PDF documentation using [Sphinx](https://www.sphinx-doc.org/) and its [Autodoc extension](https://www.sphinx-doc.org/en/master/usage/quickstart.html#autodoc), but are generally harder to work with in the source code.

This extension alleviates this drawback by highlighting select Sphinx and [reStructuredText](https://docutils.sourceforge.io/rst.html) directives within Python docstrings.

## Compatibility Notes

This extension is only compatible with the default VS Code [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension. It is **not** compatible with [Python for VSCode](https://marketplace.visualstudio.com/items?itemName=tht13.python), see #6 for details.

## Release Notes

### 0.1.1

#### Bugfixes

- Parameters ending in numbers will now be highlighted properly ([#4](https://github.com/leonhard-s/python-sphinx-highlighter/issues/4))
- Fixed parameters using wildcard notation (`*args`, `**kwargs`) not being recognized as sphings tags ([#4](https://github.com/leonhard-s/python-sphinx-highlighter/issues/4))
- Inline formatting will no longer be applied when the control characters are surrounded by whitespace ([#5](https://github.com/leonhard-s/python-sphinx-highlighter/issues/5))

### 0.1.0

Initial release
