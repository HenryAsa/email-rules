import textwrap
import os

def add_xml_comment(comment_text: str):
    """
    Converts the string `comment_text` to be formatted like an xml comment
    which can be added to the xml file
    """
    return f'<!-- {comment_text} -->'

def indent(multiline_text: str, amount: int = 1, indent_character: str = "\t") -> str:
    """
    Given a multiline string (`multiline_text`), this function will return
    that same multiline string but with `amount` `indent_character`s at each
    new line (`"\\n"`) in the string.
    """
    return textwrap.indent(multiline_text, amount * indent_character)
