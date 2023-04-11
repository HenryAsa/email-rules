
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
    final_rule : `str`
        String representing the final formatted rule
    emails_list : `list[str]`
        List of email addresses that the mail rule applies to
    concatenated_emails : `str`
        String of email addresses that are concatenated together
    rule_header : `str`
        Generic string that precedes the unique section of mail rules
    rule_footer : `str`
        Generic string that appends the unique section of mail rules


    """

    def __init__(self, list_of_emails: list = None, rule_defaults: dict = {}, rule_name: str = "Mail Filter") -> None:
        """Initialize a new Rule object

        Parameters
        ----------
        list_of_emails : `list`, optional
            list of email address to apply rule to, by default `None`
        rule_defaults : `dict`, optional
            dictionary containing default rule attributes, by default `{}`
        rule_name : `str`, optional
            name of the mail rule, by default `"Mail Filter"`
        """
        self.name: str = rule_name
        """This `str` is the title of the rule"""

        self._attribute_order: tuple[str] = ("label", "from", "subject", "hasTheWord", "doesNotHaveTheWord", "shouldNeverSpam", "shouldArchive", "sizeOperator", "sizeUnit")
        """Hard-coded order that the rule attributes should appear in"""

        self._possible_attributes: frozenset[str] = frozenset(self._attribute_order)
        """`frozenset` of the valid attributes defined in `self._attribute_order`"""

        self.rule_attributes: dict[str, str] = {}
        """This is a `dict` of all of the rule attributes that should be applied"""

        for default_attribute_name, default_attribute_value in rule_defaults.items():
            self.add_attribute(default_attribute_name, default_attribute_value)

        ###### CHECK WHETHER RULE RELIES ON SPECIFIC EMAIL ADDRESSES ######
        self.emails_list: list[str] = []
        """Flattened `list` of emails that will be included in the mail rule"""

        self.concatenated_emails: str = ""
        """A `str` of the concatenated email addresses that this rule applies to"""

        if list_of_emails is not None:
            # THIS IS THE CASE WHEN SPECIFIC EMAILS ARE PARSED INTO THE FUNCTION
            self.emails_list = self.flatten_list(list_of_emails)
            self.concatenated_emails = self.concatenate(self.emails_list)
            self.add_attribute("from", self.concatenated_emails)
        ###### CHECK WHETHER RULE RELIES ON SPECIFIC EMAIL ADDRESSES ######

        self.rule_header: str = f"{_hp.add_xml_comment(self.name)}\n<entry>\n\t<category term='filter'></category>\n\t<title>{self.name}</title>\n\t<content></content>"
        """This is a `str` representing the top section of a mail rule that remains constant"""

        self.rule_footer: str = "\n</entry>"
        """This is a `str` representing how each mail rule will end"""

    @property
    def rule_attributes_xmls(self) -> dict:
        """Converts `dict` of rule attributes into `dict` of attributes where keys are in xml format

        Returns
        -------
        rule_attribute_xmls : `dict`
        """
        rule_attributes_xmls = {}
        for attribute_name, attribute_value in self.rule_attributes.items():
            rule_attributes_xmls[attribute_name] = f"{self.xml_format_rule_attribute(attribute_name, attribute_value)}"

        return rule_attributes_xmls
    
    @property
    def rule_attributes_xmls_str(self) -> str:
        """Converts `dict` of rule attributes into ordered `str` for use in final xml

        Returns
        -------
        rule_attribute_xmls_str : `str`
        """
        rule_attributes_xmls_str = ""
        current_rule_xmls = self.rule_attributes_xmls

        for attribute_name in self._attribute_order:
            if attribute_name in current_rule_xmls:
                rule_attributes_xmls_str += current_rule_xmls[attribute_name]

        return rule_attributes_xmls_str

    @property
    def final_rule_str(self) -> str:
        """This is the final `str` that can be copied and pasted into an xml to define the rule"""
        return self.build_rule()

    def _modify_possible_attributes(self, new_attribute: str) -> None:
        """Modify the order of the hard-coded attributes arrays

        Parameters
        ----------
        new_attribute : str
            This is the attribute to add the hard-coded array
        """
        self._attribute_order = self._attribute_order + (new_attribute,)
        self._possible_attributes = frozenset(self._attribute_order)

    def flatten_list(self, list_to_flatten: list | list[list]) -> list:
        """
        This function takes a `list` (of potentially nested lists) and recursively
        flattens the list so that it is just a single list of elements that are not
        of type `list`
        """
        if list_to_flatten == []:
            return list_to_flatten

        if isinstance(list_to_flatten[0], list):
            return self.flatten_list(list_to_flatten[0]) + self.flatten_list(list_to_flatten[1:])

        return list_to_flatten[:1] + self.flatten_list(list_to_flatten[1:])

    def concatenate(self, elements_input: list, separator: str = " OR ") -> str:
        """
        Given a list of elements `elements`, this returns the concatenation of the elements with a
        separator `separator` between them (`" OR "` by default)

        Parameters
        ----------
        elements_input : `list`
            This is a list of items that should be concatenated together.
        separator : `str`, default = `" OR "`, optional
            This is the string that will be used to separate individual elements.

        Returns
        -------
        final_output : `str`
            Returns a singular string containing all of the items in `elements` after being
            concatenated and separated with the `separator`
        """
        final_string = ""

        if elements_input == []:
            return ""

        else:
            elements = self.flatten_list(elements_input)

            for element in elements:
                final_string += f"{element}{separator}"

            final_output = final_string[:-len(separator)]

            return final_output

    def xml_format_rule_attribute(self, name: str, value: str) -> str:
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

        Returns
        ----------
        rule_line : `str`
            Returns the properly formatted attribute
        """
        rule_line = f"\n\t<apps:property name='{name}' value='{value}'/>"

        return rule_line
    
    def add_attribute(self, name: str, value: str, is_custom_attribute: bool = False) -> None:
        """Add an attribute to the mail rule

        Parameters
        ----------
        name : str
            Name of the attribute to add
        value : str
            Value of the attribute
        is_custom_attribute : bool, optional
            Defines whether the attribute being added is custom (use with caution), default = `False`
        """
        if name in self.rule_attributes:
            ## Raise Error when rule already contains a value for this attribute
            raise KeyError(f"{name} is already an attribute of {self.name}.  Consider calling self.update_attribute() to update the value of this attribute")

        if is_custom_attribute:
            ## Check whether we are using a custom attribute
            if name not in self._possible_attributes:
                ## Add custom attribute name to the possible rule attributes
                self._modify_possible_attributes(name)

        if name not in self._possible_attributes:
            ## Raise Error if this attribute name is unallowed
            raise KeyError(f"{name} is not a valid filter attribute.  Check for typos")

        self.rule_attributes[name] = value

    def build_rule(self) -> str:
        """
        After all of the details of a rule are defined, this function is run
        to actually build the desired mail rule.  It takes an optional argument
        `rule_name` which is a `str` representing the name of the mail rule,
        but when the rule is parsed into Gmail, this gets ignored.
        """
        final_rule = f"{self.rule_header}{self.rule_attributes_xmls_str}{self.rule_footer}"
        final_rule = final_rule.expandtabs(_hp.TAB_SPACING)

        return final_rule
