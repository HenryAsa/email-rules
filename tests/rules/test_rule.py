import pytest

from gmail_rules.rules.rule import Rule

class test_rule:

    def test_rule_definition(self):
        new_rule = Rule()
        assert isinstance(new_rule, Rule)
