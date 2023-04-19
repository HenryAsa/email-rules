
from gmail_rules.actions import set_module
import gmail_rules.rules as _R
import gmail_rules.utils.helpers as _hp
import torch

torch.nn.ModuleList
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
    def final_string(self):
        """Generates the final string representation of a collection of rules

        Returns
        -------
        str
            `str` representing the xmls of all the rules in this collection
        """
        return self.build_final_string()

    #### TODO: FIX THIS TO ACCOUNT FOR INDENTING ####
    def add_rule(self, rules_to_add: _R.Rule | list[_R.Rule]):
        try:
            if isinstance(rules_to_add, _R.Rule):
                rules_to_add = [rules_to_add]
            elif isinstance(rules_to_add[0], _R.Rule):
                pass
            else:
                raise TypeError(f"rule_to_add is not of type Rule or a list of Rules.  It is of type {type(rules_to_add)}")

        except TypeError:
            raise TypeError(f"rule_to_add is not of type Rule or a list of Rules.  It is of type {type(rules_to_add)}")

        for rule in rules_to_add:
            if rule.name in self.rules_dict:
                raise KeyError(f"{rule.name} is already in the collection of rules.  Use update_rule() to change the value of this rule")
            else:
                self.rules_list.append(rule)
                self.rules_dict[rule.name] = rule

    def build_final_string(self, additional_comment: str = None):
        final_string = ""

        for rule in reversed(self.rules_list):      ## MAYBE REMOVE REVERSAL
            final_string += f"\n\n{rule.build_rule()}"

        if additional_comment is not None:
            final_string = f"{_hp.add_xml_comment(additional_comment)}"

        return final_string
    #### TODO: FIX THIS TO ACCOUNT FOR INDENTING ^^^ ####
