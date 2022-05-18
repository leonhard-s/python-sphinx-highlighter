# The following lines should all be highlighted as tags:

"""

:param:                         This tag does not have a name.
:param p1:                      Ends in a number.
:param dict_:                   Ends in an underscore.
:param dict\\_:                 Ends in an escaped underscore.
:param *args:                   Starts with an asterisk.
:param \\*args:                 Starts with an escaped asterisk.
:param **kwargs:                Starts with two asterisks.
:param \\*\\*kwargs:            Starts with two escaped asterisks.
:param _test:                   Starts with an underscore.
:param \\_test:                 Starts with an escaped underscore.
:param __test:                  Starts with two underscores.
:param \\__test:                Starts with two escaped underscores.

"""

# The following tags should not be highlighted:

"""

:param 123:                     Integer literal.
:param 1.0:                     Float literal.
:param 1two3:                   Starts with a numeric character.
:param 'value':                 This parameter contains quotes.
:meth:`MyClass.method`          This is a reference and not a tag.

"""
