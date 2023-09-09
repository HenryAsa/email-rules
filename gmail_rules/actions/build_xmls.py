from distutils.command import build
from ..utils import helpers as _hp

__all__ = ["build_xml_text"]

def build_xml_text(text: str) -> str:
    """
    Build a final string that can be pasted into a .xml file from the strings
    returned by the `build_rule()` methods in the `Rule` classes
    """
    final_text = f"<?xml version='1.0' encoding='UTF-8'?>\n<feed xmlns='http://www.w3.org/2005/Atom' xmlns:apps='http://schemas.google.com/apps/2006'>\n\t<title>Mail Filters</title>\n\t<author>\n\t\t<name>{_hp.AUTHOR_NAME}</name>\n\t\t<email>{_hp.AUTHOR_EMAIL}</email>\n\t</author>\n{_hp.indent(text)}\n</feed>".expandtabs(_hp.TAB_SPACING)

    return final_text

# def build_mail_rule_file(filename: str) -> None:
#     xml_text = f"{build_xml_text(final_string)}"

#     current_directory = os.getcwd()
#     f = open(f"{current_directory}/New Rules/Rule XMLs/{filename}.xml", "w")
#     f.write(xml_text)
#     f.close()