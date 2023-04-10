import textwrap
import os

TAB_SPACING = 4

def add_xml_comment(comment_text: str) -> str:
    """Add an xml comment to a string (does not include for newlines `"\\n"`)

    Parameters
    ----------
    comment_text : `str`
        Text that will be added as a comment

    Returns
    -------
    `str`
        xml comment of `comment_text`
    """
    return f'<!-- {comment_text} -->'

def indent(multiline_text: str, amount: int = 1, indent_character: str = "\t") -> str:
    """Indents a string with `amount` `indent_character`s

    Prefix each newline (`"\\n"`) in multiline_text with `amount * indent_character`

    Parameters
    ----------
    multiline_text : `str`
        Multiline `str` containing `"\\n"` that should be indented
    amount : `int`, optional
        The amount that `multiline_text` should be indented by, defaulted to 1
    indent_character : `str`, optional
        The character that `multiline_text` should be indented with, defaulted to `"\\t"`

    Returns
    -------
    str
        The texted indented with `amount` instances of the `indent_character`
    """
    return textwrap.indent(multiline_text, amount * indent_character)
