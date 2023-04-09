
from gmail_rules.utils import helpers as _hp
from . import set_module

__all__ = ["Rule"]

@set_module('gmail_rules.rules')
class Rule:
    """Defines an individual mail rule and its necessary attributes

    A rule class defines an individual mail rule and includes functions/operations
    to modify a rule's behavior and generate parseable formats of a rule.

    ...

    Attributes
    ----------
    name : `str`
        Name of the mail rule.
    final_rule : `str`, optional
        String representing the final formatted rule
    emails_list : `list[str]`
        List of email addresses that the mail rule applies to
    concatenated_emails : `str`
        String of email addresses that are concatenated together
    from_attribute : `str`
        A specific string designated to hold the 'from' mail rule attribute
    rule_header : `str`
        Generic string that precedes the unique section of mail rules
    rule_footer : `str`
        Generic string that appends the unique section of mail rules


    """

    def __init__(self, list_of_emails: list = None, rule_flags: dict = {}, rule_name: str = "Mail Filter") -> None:
        """Initialize a new Rule object

        Parameters
        ----------
        list_of_emails : `list`, optional
            list of email address to apply rule to, by default `None`
        rule_flags : `dict`, optional
            boolean rule flags to add to rule, by default `{}`
        rule_name : `str`, optional
            name of the mail rule, by default `"Mail Filter"`
        """
        self.name: str = rule_name
        """This `str` is the title of the rule"""

        self.final_rule: str = ""
        """This is the final `str` that can be copied and pasted into an xml to define the rule"""

        ###### CHECK WHETHER RULE RELIES ON SPECIFIC EMAIL ADDRESSES ######
        self.emails_list: list[str] = []
        """Flattened `list` of emails that will be included in the mail rule"""

        self.concatenated_emails: str = ""
        """A `str` of the concatenated email addresses that this rule applies to"""

        self.from_attribute: str = ""
        """This `str` is the attribute associated with a rule that uses 'from' (which is many of them)"""

        if list_of_emails is not None:
            # THIS IS THE CASE WHEN SPECIFIC EMAILS ARE PARSED INTO THE FUNCTION
            self.emails_list = self.flatten_list(list_of_emails)
            self.concatenated_emails = self.concatenate(self.emails_list)
            self.from_attribute = self.define_rule_attribute("from", self.concatenated_emails, True)
        ###### CHECK WHETHER RULE RELIES ON SPECIFIC EMAIL ADDRESSES ######

        self.rule_header: str = f"{_hp.add_xml_comment(self.name)}\n<entry>\n\t<category term='filter'></category>\n\t<title>{self.name}</title>\n\t<content></content>"
        """This is a `str` representing the top section of a mail rule that remains constant"""

        self.rule_footer: str = "\n</entry>"
        """This is a `str` representing how each mail rule will end"""

        self.rule_attributes: list[str] = []
        """This is a `list` of all of the rule attribute strings that should be applied"""

        self.rule_specific_attributes: str = ""
        """This is a `str` representing attributes that are always applied to a specific type of rule"""

        self.flags_dict: dict[str, str] = rule_flags
        """This is a `dict` representing all of the flags that are going to be applied to this rule"""

        self.flags: str = self.parse_flags()
        """This is a `str` representing boolean rule attributes that are initialized early on"""

    def parse_flags(self) -> str:
        """Convert dictionary of rule flags into string standard attributes

        Returns
        -------
        flags_string : str
        """
        flags_string = ""
        for attribute_name, attribute_value in self.flags_dict.items():
            flags_string += f"{self.define_rule_attribute(attribute_name, attribute_value, True)}"
        return flags_string

    def flatten_list(self, list_to_flatten: list) -> list:
        """
        This function takes a `list` (of potentially nested lists) and recursively
        flattens the list so that it is just a single list of elements that are not
        of type list
        """
        if list_to_flatten == []:
            return list_to_flatten

        if isinstance(list_to_flatten[0], list):
            return self.flatten_list(list_to_flatten[0]) + self.flatten_list(list_to_flatten[1:])

        return list_to_flatten[:1] + self.flatten_list(list_to_flatten[1:])

    def concatenate(self, elements_input: list = None, separator: str = " OR ") -> str:
        """
        Given a list of elements `elements`, this returns the concatenation of the elements with a
        separator `separator` between them (`" OR "` by default).  Defaults to concaenating
        `self.emails_list` but can also take in a list of elements.

        Parameters
        ----------
        elements_input : `list`, default = `None`, optional
            This is a list of items that should be concatenated together.
        separator : `str`, default = `" OR "`, optional
            This is the string that will be used to separate individual
            elements.

        Returns
        -------
        final_output : `str`
            Returns a singular string containing all of the items in `elements` after being
            concatenated and separated with the `separator`.  Also assigns a new value to
            `self.concatenated_emails` depending on whether email addresses were being
            concatenated.
        """
        final_string = ""

        if elements_input is None:
            elements = self.emails_list

            if elements == []:
                return ""

        else:
            elements = self.flatten_list(elements_input)

        for element in elements:
            final_string += f"{element}{separator}"

        final_output = final_string[:-len(separator)]

        if elements_input is None:
            self.concatenated_emails = final_output
            self.from_attribute = self.define_rule_attribute("from", final_output, True)

        return final_output

    def define_rule_attribute(self, name: str, value: str, exclude_from_attributes: bool = False) -> str:
        """
        Given an attribute name, its value, and an optional boolean determining whether this
        new attriute should be added to the list of attributes, this function properly builds
        and formats (and assigns) the defined attribute.

        Parameters
        ----------
        name : `str`
            This is the name of the attribute to define (defined by Google's docs)
        value : `str`
            This is the value of the desired attribute
        exclude_from_attributes : `bool`, default = `False`, optional
            This boolean parameter determines whether or not the newly defined attribute
            should be appended to the `self.rule_attributes` list or whether the newly
            defined attribute should be returned as `str`

        Returns
        ----------
        rule_line : `str`, optional
            Returns the properly formatted attribute if and only if `exclude_from_attributes`
            is `True` (which it is not by default).  Otherwise simply appends `rule_line` to
            the `self.rule_attributes` list
        """
        rule_line = f"\n\t<apps:property name='{name}' value='{value}'/>"

        if not exclude_from_attributes:
            self.rule_attributes.append(rule_line)

        return rule_line

    def build_rule(self) -> str:
        """
        After all of the details of a rule are defined, this function is run
        to actually build the desired mail rule.  It takes an optional argument
        `rule_name` which is a `str` representing the name of the mail rule,
        but when the rule is parsed into Gmail, this gets ignored.
        """
        self.concatenate()
        final_rule = self.rule_header

        final_rule += self.from_attribute

        for rule_attribute in self.rule_attributes:
            final_rule += f"{rule_attribute}"

        final_rule += f"{self.rule_specific_attributes}{self.flags}{self.rule_footer}"
        final_rule = final_rule.expandtabs(TAB_SPACING)

        self.final_rule = final_rule

        return final_rule
