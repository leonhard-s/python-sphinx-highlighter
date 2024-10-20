# pylint: disable=pointless-string-statement

# The following lines should all be `entity.name.tag.sphinx`:

"""
:a:                             Very short tag.
:py:                            Slightly less short tag.
:foo:                           Short tag.
:param:                         This tag has no value
"""

# These are not valid tags and should not be highlighted:

"""
:1:
:\\a:
"""

# Tags with values (e.g. for parameters), should be `entity.name.tag.sphinx`
# for the tag and `entity.name.tag.value.sphinx` for the value:

"""
:param a:                       This tag's value is a single char
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

# Tags with values and parameter type information. The type information should
# be `entity.name.tag.value.type.sphinx`:

"""
:param a b:                     This tag has two values
:param float value:             This tag has type information
"""


# The following tags should be treated as tags with references:

"""

:param 123:                     Integer literal.
:param 1.0:                     Float literal.
:param 1two3:                   Starts with a numeric character.
:param 'value':                 This parameter contains quotes.

"""
