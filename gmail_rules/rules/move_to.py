
from ..utils import helpers as _hp
from ..rules.rule import Rule as _Rule

__all__ = ["Move_To"]

class Move_To(_Rule):
    """:obj:`Move_To` rule object which is a sub-class of :obj:`Rule`
    """

    def __init__(self, rule_label: str | list, list_of_emails: list = [], rule_defaults: dict = {}, rule_name: str = "") -> None:
        """Initialize a :obj:`Move_To` rule object which is a subclass of :obj:`Rule`

        Parameters
        ----------
        rule_label : `str` or `list`
            This is the label that should be applied to emails that meet
            this rule's criteria
        list_of_emails : `list`, optional
            This is a list of email addresses that the mail rule should be
            applied to
        rule_defaults : `dict`, optional
            This is a dictionary containing default rule attributes
        rule_name : `str`, optional
            This is the name of the specific rule
        """
        if rule_name == "":
            rule_name = "MOVE TO: "

            if isinstance(rule_label, str):
                rule_name += f"{rule_label}"

            elif type(rule_label) in _hp.ITERABLE_DATA_TYPES:
                for label in rule_label:
                    rule_name += f"{label} | "
                rule_name = rule_name[:-3]

        rule_defaults.update(shouldNeverSpam = "true", shouldArchive = "true")
        ## Add rule-type specific flags to the flags dictionary

        super().__init__(list_of_emails, rule_defaults, rule_name)

        self.add_labels(rule_label)
        ## Add the label attribute to the mail rule
