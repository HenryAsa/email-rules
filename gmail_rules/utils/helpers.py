import textwrap

TAB_SPACING : int = 4
"""Default amount of spaces used instead of a tab (`"\\t"`)"""
ITERABLE_DATA_TYPES : set = {list, tuple, set, frozenset, dict}
"""Iterable data types that can store multiple instances of other objects\n\nContains: `list`, `tuple`, `set`, `frozenset`, `dict`"""

def add_xml_comment(comment_text: str) -> str:
    """Add an xml comment to a string (does not include for newlines `"\\n"`)

    Parameters
    ----------
    comment_text : str
        Text that will be added as a comment

    Returns
    -------
    str
        xml comment of `comment_text`
    """
    return f'<!-- {comment_text} -->'

def indent(multiline_text: str, amount: int = 1, indent_character: str = "\t") -> str:
    """Indents a string with `amount` `indent_character`

    Prefix each newline (`"\\n"`) in multiline_text with `amount * indent_character`

    Parameters
    ----------
    multiline_text : str
        Multiline str containing `"\\n"` that should be indented
    amount : int, optional
        The amount that `multiline_text` should be indented by, defaulted to 1
    indent_character : str, optional
        The character that `multiline_text` should be indented with, defaulted to `"\\t"`

    Returns
    -------
    str
        The texted indented with `amount` instances of the `indent_character`
    """
    return textwrap.indent(multiline_text, amount * indent_character)

def convert_to_parseable_string(string_to_parse: str) -> str:
    """Converts a rich-text string into a parseable string containing tabs and newlines

    This function takes a string and allows newlines/tabs to be displayed as `\\n` and `\\t`
    rather than a newline and a tab

    Parameters
    ----------
    string_to_parse : str
        String to display parsed richtext operations for

    Returns
    -------
    str
        String displaying `\\n` and `\\t` rather than newlines and tabs
    """
    final_string = string_to_parse
    final_string = final_string.replace("\n", "\\n").replace("\t", "\\t").replace("    ", "\\t")
    return final_string
