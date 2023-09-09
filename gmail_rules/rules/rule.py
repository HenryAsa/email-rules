
from ..utils import helpers as _hp
from ..rules import set_module

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
    emails_list : `list`
        List of email addresses (:obj:`str`) that the mail rule applies to
    concatenated_emails : `str`
        String of email addresses that are concatenated together
    rule_header : `str`
        Generic string that precedes the unique section of mail rules
    rule_footer : `str`
        Generic string that appends the unique section of mail rules


    """

    def __init__(self, list_of_emails: list = [], rule_defaults: dict = {}, rule_name: str = "Mail Filter") -> None:
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
        self.labels: list = []
        """This is a `list` containing all of the labels that should be applied to this rule"""

        self.name: str = rule_name
        """This `str` is the title of the rule"""

        self._attribute_order: tuple = ("label", "from", "subject", "hasTheWord", "doesNotHaveTheWord", "shouldNeverSpam", "shouldArchive", "sizeOperator", "sizeUnit")
        """Hard-coded order that the rule attributes should appear in"""

        self._possible_attributes: frozenset = frozenset(self._attribute_order)
        """`frozenset` of the valid attributes defined in `self._attribute_order`"""

        self.rule_attributes: dict[str, str] = {}
        """This is a `dict` of all of the rule attributes that should be applied"""

        for default_attribute_name, default_attribute_value in rule_defaults.items():
            self.add_attribute(default_attribute_name, default_attribute_value)

        ###### CHECK WHETHER RULE RELIES ON SPECIFIC EMAIL ADDRESSES ######
        self.emails_list: list = self.flatten_list(list_of_emails)
        """Flattened `list` of emails that will be included in the mail rule"""

        self.concatenated_emails: str = self.concatenate(self.emails_list)
        """A `str` of the concatenated email addresses that this rule applies to"""

        if list_of_emails != []:
            # THIS IS THE CASE WHEN SPECIFIC EMAILS ARE PARSED INTO THE FUNCTION
            self.add_attribute("from", self.concatenated_emails)
        ###### CHECK WHETHER RULE RELIES ON SPECIFIC EMAIL ADDRESSES ######

        self.rule_header: str = f"<entry>\n\t<category term='filter'></category>\n\t<title>{self.name}</title>\n\t<content></content>"
        """This is a `str` representing the top section of a mail rule that remains constant"""

        self.rule_footer: str = "\n</entry>"
        """This is a `str` representing how each mail rule will end"""

    @property
    def rule_attributes_xmls(self) -> dict:
        """Converts `dict` of rule attributes into `dict` of attributes where keys are in xml format

        Returns
        -------
        rule_attribute_xmls : `dict`
            Dictionary where keys are the attribute and values are the xml representation of the attribute
        """
        rule_attributes_xmls = {}
        for attribute_name, attribute_value in self.rule_attributes.items():
            rule_attributes_xmls[attribute_name] = f"{self.xml_format_rule_attribute(attribute_name, attribute_value)}"

        return rule_attributes_xmls

    @property
    def rule_attributes_xmls_str(self) -> str:
        """Converts :obj:`dict` of rule attributes into ordered `str` for use in final xml

        Returns
        -------
        rule_attribute_xmls_str : `str`
            :obj:`str` representing this :obj:`Rule` as an xml
        """
        rule_attributes_xmls_str = ""
        current_rule_xmls = self.rule_attributes_xmls

        for attribute_name in self._attribute_order:
            if attribute_name in current_rule_xmls:
                rule_attributes_xmls_str += current_rule_xmls[attribute_name]

        return rule_attributes_xmls_str

    @property
    def final_rule_str(self) -> str:
        """This is the final `str` that can be copied and pasted into an xml to define the rule

        Returns
        -------
        str
            `str` representing the entire rule in xml format
        """
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

    def flatten_list(self, list_to_flatten: list) -> list:
        """Converts a list of lists into a single flat list

        This function takes a `list` (of potentially nested lists) and recursively
        flattens the list so that it is just a single list of elements that are not
        of type `list`

        Parameters
        ----------
        list_to_flatten : `list`
            Input `list` (or list of lists) to be flattened
        
        Returns
        -------
        list
            Returns a final flat list that does not contain any nested lists
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
            This is a list of items that should be concatenated together
        separator : `str`, default = `" OR "`, optional
            This is the string that will be used to separate individual elements, by default `" OR "`

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
        -------
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
            Defines whether the attribute being added is custom (use with caution), by default `False`.
            Use this with caution, as the mail rule interpreter may not be able to parse a rule with
            a custom attribute

        Raises
        ------
        KeyError
            Raises a `KeyError` when an attribute has already been defined for this rule
        KeyError
            Raises a `KeyError` if an attribute is not valid
        """
        if name in self.rule_attributes:
            ## Raise Error when rule already contains a value for this attribute
            raise KeyError(f"{name} is already an attribute of {self.name}.  Consider calling {self.__class__.__name__}.update_attribute() to update the value of this attribute")

        if is_custom_attribute:
            ## Check whether we are using a custom attribute
            if name not in self._possible_attributes:
                ## Add custom attribute name to the possible rule attributes
                self._modify_possible_attributes(name)

        if name not in self._possible_attributes:
            ## Raise Error if this attribute name is unallowed
            raise KeyError(f"{name} is not a valid filter attribute.  Check for typos")

        if name == "label":
            ## Labels are stored in self.labels, not in self.rule_attributes
            # raise KeyError(f"Use {self.__class__.__name__}.add_label() or {self.__class__.__name__}.add_labels() to add a label to the rule")
            self.add_labels(value)
            return

        self.rule_attributes[name] = value

    def add_attributes(self, attributes_to_add: dict) -> None:
        """Add multiple attributes to a `Rule`

        Parameters
        ----------
        attributes_to_add : dict
            Dictionary where key is the name of the attribute to add (`str`)
            and its value (`str`) is the value of the attribute to add corresponding
            to that key

        Raises
        ------
        TypeError
            Raises a `TypeError` if `attributes_to_add` is not a dictionary
        """
        if not isinstance(attributes_to_add, dict):
            raise TypeError(f"attributes_to_add needs to be a dictionary, but currently it is of type {type(attributes_to_add)}")

        for attribute_name, attribute_value in attributes_to_add.items():
            self.add_attribute(attribute_name, attribute_value)

    def add_labels(self, labels: str | list | tuple | set | frozenset | dict) -> None:
        """Adds labels to the mail rule

        Parameters
        ----------
        labels : list | tuple | set | frozenset | dict
            The label (or labels) to be added to the rule

        Raises
        ------
        TypeError
            Raises a `TypeError` if the label is not a valid type
        """
        if isinstance(labels, str):
            self.labels.append(labels)

        elif type(labels) in _hp.ITERABLE_DATA_TYPES:
            for label in labels:
                self.add_labels(label)

        else:
            raise TypeError(f"The label being added is not a string.  It is of type {type(label)}")

    def add_label(self, label: str) -> None:
        """Alias for :obj:`Rule.add_label()`.  Adds labels to the mail rule

        Parameters
        ----------
        labels : list | tuple | set | frozenset | dict
            The label (or labels) to be added to the rule

        Raises
        ------
        TypeError
            Raises a `TypeError` if the label is not a valid type
        """
        self.add_labels(label)

    def build_rule(self) -> str:
        """
        After all of the details of a rule are defined, this function is run
        to actually build the desired mail rule.  It takes an optional argument
        `rule_name` which is a `str` representing the name of the mail rule,
        but when the rule is parsed into Gmail, this gets ignored.
        """
        final_rule = ""

        if not self.labels:
            final_rule += f"{_hp.add_xml_comment(self.name)}\n{self.rule_header}{self.rule_attributes_xmls_str}{self.rule_footer}"

        else:
            for label in self.labels:
                rule_comment = _hp.add_xml_comment(self.name if len(self.labels) == 1 else f'{self.name} ({label})')
                final_rule += f"{rule_comment}\n{self.rule_header}{self.xml_format_rule_attribute('label', label)}{self.rule_attributes_xmls_str}{self.rule_footer}\n"

            final_rule = final_rule[:-1]

            if len(self.labels) > 1:
                starting_comment = f"{_hp.add_xml_comment(f'START --- {self.name} --- START')}\n"
                ending_comment = f"\n{_hp.add_xml_comment(f'END --- {self.name} --- END')}"
                final_rule = f"{starting_comment}{final_rule}{ending_comment}"

        final_rule = final_rule.expandtabs(_hp.TAB_SPACING)

        return final_rule
