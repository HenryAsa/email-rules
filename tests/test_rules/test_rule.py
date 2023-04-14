import pytest

from gmail_rules.rules.rule import Rule
import gmail_rules.utils.helpers as _hp

class TestRule:

    def test_rule_definition(self):
        new_rule = Rule()
        assert isinstance(new_rule, Rule)

    def test_add_rule_attribute(self):
        correct_rule = "<!-- Mail Filter -->\n<entry>\n\t<category term='filter'></category>\n\t<title>Mail Filter</title>\n\t<content></content>\n\t<apps:property name='subject' value='Meow'/>\n\t<apps:property name='hasTheWord' value='Bla bla'/>\n\t<apps:property name='doesNotHaveTheWord' value='Three'/>\n\t<apps:property name='shouldNeverSpam' value='false'/>\n</entry>".expandtabs(_hp.TAB_SPACING)

        new_rule = Rule()
        new_rule.add_attribute("subject", "Meow")
        new_rule.add_attribute("hasTheWord", "Bla bla")
        new_rule.add_attribute("doesNotHaveTheWord", "Three")
        new_rule.add_attribute("shouldNeverSpam", "false")

        assert new_rule.final_rule_str == correct_rule

    def test_add_rule_attributes_unordered(self):
        correct_rule = "<!-- Mail Filter -->\n<entry>\n\t<category term='filter'></category>\n\t<title>Mail Filter</title>\n\t<content></content>\n\t<apps:property name='subject' value='Meow'/>\n\t<apps:property name='hasTheWord' value='Bla bla'/>\n\t<apps:property name='doesNotHaveTheWord' value='Three'/>\n\t<apps:property name='shouldNeverSpam' value='false'/>\n</entry>".expandtabs(_hp.TAB_SPACING)

        new_rule = Rule()
        new_rule.add_attribute("shouldNeverSpam", "false")
        new_rule.add_attribute("hasTheWord", "Bla bla")
        new_rule.add_attribute("subject", "Meow")
        new_rule.add_attribute("doesNotHaveTheWord", "Three")

        assert new_rule.final_rule_str == correct_rule
