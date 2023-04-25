
from gmail_rules.actions import set_module
import gmail_rules.rules as _R
import gmail_rules.utils.helpers as _hp

@set_module("gmail_rules.actions")
class Rule_Collection:
    """Collection of :obj:`Rule`s that can be organized and stored together

    Parameters
    ----------
    name : :obj:`str`, optional
        Name of this collection of rules
    """

    def __init__(self, name: str = "Rule Collection") -> None:
        self.name = name
        """`str` representing the name of the collection of rules"""

        self.rules_list: list[_R.Rule] = []
        """`list` of `Rule` objects that will be included in a single file"""

        self.rules_dict: dict[str, _R.Rule] = {}
        """`dict` where keys are a rule's title (`rule_title`) and the values are that rule"""

    def __getitem__(self, name: str) -> _R.Rule:
        """Allows easy retrieval of :obj:`Rule`s stored in a `Rule_Collection`

        Gets the :obj:`Rule` stored in `self.rules_dict[name]`.  Can retreive a rule
        from a collection by running `Rule_Collection[rule_name]`

        Parameters
        ----------
        name : str
            Name of the rule to be retrieved

        Returns
        -------
        _R.Rule
            :obj:`Rule` with the corresponding name
        """
        return self.rules_dict[name]

    @property
    def final_string(self) -> str:
        """Generates the final string representation of a collection of rules

        Returns
        -------
        str
            `str` representing the xmls of all the rules in this collection
        """
        return self.build_final_string()

    #### TODO: FIX THIS TO ACCOUNT FOR INDENTING ####
    def add_rule(self, rule_to_add: _R.Rule) -> None:
        """Add a :obj:`Rule` to a `Rule_Collection`

        Parameters
        ----------
        rule_to_add : :obj:`Rule`
            This is the rule that should be added to this collection

        Raises
        ------
        TypeError
            Raises a `TypeError` if `rule_to_add` is not of type :obj:`Rule`
        KeyError
            Raises a `KeyError` if `rule_to_add` is already in the :obj:`Rule_Collection`
        """
        if not isinstance(rule_to_add, _R.Rule):
            raise TypeError(f"rule_to_add is not of type Rule.  It is of type {type(rule_to_add)}")
        if rule_to_add.name in self.rules_dict:
            raise KeyError(f"{rule_to_add.name} is already in the collection of rules.  Use update_rule() to change the value of this rule")

        self.rules_dict[rule_to_add.name] = rule_to_add
        self.rules_list.append(rule_to_add)
    
    def add_rules(self, rules_to_add: list[_R.Rule]) -> None:
        """Add multiple :obj:`Rule` objects to the collection at once

        Parameters
        ----------
        rules_to_add : list[_R.Rule]
            Iterable that contains all of the :obj:`Rule`s to be added

        Raises
        ------
        TypeError
            Raises a `TypeError` if `rules_to_add` is not an iterable datatype
        """
        if not hasattr(rules_to_add, "__iter__"):
            raise TypeError(f"rules_to_add needs to be an iterable, but currently is of type {type(rules_to_add)}")

        for rule in rules_to_add:
            self.add_rule(rule)

    def build_final_string(self, additional_comment: str = None) -> str:
        """Builds the final properly formatted collection of rules

        Parameters
        ----------
        additional_comment : str, optional
            Adds a final comment above the entire rule string, by default None

        Returns
        -------
        str
            final string representing all of the :obj:`Rule`s in the collection
        """
        final_string = ""

        if additional_comment is not None:
            final_string += f"{_hp.add_xml_comment(additional_comment)}"

        for rule in reversed(self.rules_list):      ## MAYBE REMOVE REVERSAL
            final_string += f"\n\n{rule.build_rule()}"

        return final_string
    #### TODO: FIX THIS TO ACCOUNT FOR INDENTING ^^^ ####
