# Python Sphinx Highlighter

This is an extension for [Visual Studio Code](https://code.visualstudio.com/) designed to improve readability of [Python](https://www.python.org/) docstrings using the [Sphinx docstring format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html).

## Features

![Sphinx docstring highlight comparison](images/comparison.gif)

*The source code shown is the example from the [Read the Docs Sphinx docstring format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html#an-example-class-with-docstrings) introduction.*

Sphinx docstrings are compact and can easily be converted into HTML or PDF documentation using [Sphinx](https://www.sphinx-doc.org/) and its [Autodoc extension](https://www.sphinx-doc.org/en/master/usage/quickstart.html#autodoc), but are generally harder to work with in the source code.

This extension alleviates this drawback by highlighting select Sphinx and [reStructuredText](https://docutils.sourceforge.io/rst.html) directives within Python docstrings.

## Compatibility Notes

This extension is only compatible with the default VS Code [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension. It is **not** compatible with [Python for VSCode](https://marketplace.visualstudio.com/items?itemName=tht13.python), see [#6](https://github.com/leonhard-s/python-sphinx-highlighter/issues/6) for details.

## Release Notes

### v0.3.0

#### Changes

- Multi-word tag values (such as `:param int y:`) are now permitted. This is used by Sphinx autodoc to include the argument type in a single line:

    ```py
    def foo(x, y):
        """
        :param int x: Argument with autodoc shorthand

        :param y: Argument with separate type tag
        :type y: int
        """
        ...
    ```

    Both variants are correct and highlighted when using this extension.

#### Bug fixes

- Single character tag values (such as `:param x:`) are now recognized as tags

### v0.2.0

#### Changes

- The value portion of a named tag (such as `:param arg:`) is now selectable individually via the `entity.name.tag.value.sphinx` scope ([#7](https://github.com/leonhard-s/python-sphinx-highlighter/issues/7))

#### Bug fixes

- The closing colon of a Sphinx tag will now be correctly scoped as `punctuation.definition.interpreted.sphinx` ([#8](https://github.com/leonhard-s/python-sphinx-highlighter/issues/8))

### v0.1.1

#### Bug fixes

- Parameters ending in numbers will now be highlighted properly ([#4](https://github.com/leonhard-s/python-sphinx-highlighter/issues/4))
- Fixed parameters using wildcard notation (`*args`, `**kwargs`) not being recognized as sphinx tags ([#4](https://github.com/leonhard-s/python-sphinx-highlighter/issues/4))
- Inline formatting will no longer be applied when the control characters are surrounded by whitespace ([#5](https://github.com/leonhard-s/python-sphinx-highlighter/issues/5))

### v0.1.0

Initial release
