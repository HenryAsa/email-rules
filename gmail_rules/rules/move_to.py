
from gmail_rules.utils import helpers as _hp
from gmail_rules.rules.rule import Rule as _Rule

from . import set_module

__all__ = ["Move_To"]

@set_module('gmail_rules.rules')
class Move_To(_Rule):
    """Move_To rule object which is a sub-class of :obj:`Rule`

    Parameters
    ----------
    rule_label : `str`
        This is the label that should be applied to emails that meet
        this rule's criteria
    list_of_emails : `list`
        This is a list of email addresses that the mail rule should be
        applied to.
    rule_defaults : `dict`, optional
        This is a dictionary containing default rule attributes

    Returns
    ----------
        `None`
            Doesn't return anything.
    """

    def __init__(self, rule_label: str, list_of_emails: list = None, rule_defaults: dict = {}) -> None:
        """Initialize a Move_To rule object which is a subclass of :obj:`Rule`

        Parameters
        ----------
        rule_label : `str`
            This is the label that should be applied to emails that meet
            this rule's criteria
        list_of_emails : `list`
            This is a list of email addresses that the mail rule should be
            applied to.
        rule_defaults : `dict`, optional
            This is a dictionary containing default rule attributes

        Returns
        ----------
            `None`
                Doesn't return anything.
        """
        rule_name = f"MOVE TO: {rule_label}"
        rule_defaults.update(shouldNeverSpam = "true", shouldArchive = "true")
        ## Add rule-type specific flags to the flags dictionary

        super().__init__(list_of_emails, rule_defaults, rule_name)

        self.rule_label: str = rule_label
        """This is the label that will be applied to all of the emails with this rule"""

        self.define_rule_attribute("label", self.rule_label)
        ## Add the labeling attribute to the mail rule
