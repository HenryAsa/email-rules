import pytest

from gmail_rules.rules.rule import Rule
import gmail_rules.utils.helpers as _hp

from gmail_rules.rules.copy_to import Copy_To
from gmail_rules.rules.move_to import Move_To


class TestRule:

    # @pytest.mark.parametrize("rule", [Rule(), Copy_To("label_1"), Move_To("label_1")], ids=["Rule", "Copy_To", "Move_To"])
    # def test_rule_definition(self, rule):
    def test_rule_definition(self):
        """Test creating/defining a new :obj:`Rule`
        """
        new_rule = Rule()
        assert isinstance(new_rule, Rule)

    def test_add_rule_attribute(self):
        """Test adding attributes to a :obj:`Rule` in the correct order
        """
        correct_rule = "<!-- Mail Filter -->\n<entry>\n\t<category term='filter'></category>\n\t<title>Mail Filter</title>\n\t<content></content>\n\t<apps:property name='subject' value='Meow'/>\n\t<apps:property name='hasTheWord' value='Bla bla'/>\n\t<apps:property name='doesNotHaveTheWord' value='Three'/>\n\t<apps:property name='shouldNeverSpam' value='false'/>\n</entry>".expandtabs(_hp.TAB_SPACING)

        new_rule = Rule()
        new_rule.add_attribute("subject", "Meow")
        new_rule.add_attribute("hasTheWord", "Bla bla")
        new_rule.add_attribute("doesNotHaveTheWord", "Three")
        new_rule.add_attribute("shouldNeverSpam", "false")

        assert new_rule.final_rule_str == correct_rule

    def test_add_rule_attributes_unordered(self):
        """Test adding a attributes to a :obj:`Rule` in a random order
        """
        correct_rule = "<!-- Mail Filter -->\n<entry>\n\t<category term='filter'></category>\n\t<title>Mail Filter</title>\n\t<content></content>\n\t<apps:property name='subject' value='Meow'/>\n\t<apps:property name='hasTheWord' value='Bla bla'/>\n\t<apps:property name='doesNotHaveTheWord' value='Three'/>\n\t<apps:property name='shouldNeverSpam' value='false'/>\n</entry>".expandtabs(_hp.TAB_SPACING)

        new_rule = Rule()
        new_rule.add_attribute("shouldNeverSpam", "false")
        new_rule.add_attribute("hasTheWord", "Bla bla")
        new_rule.add_attribute("subject", "Meow")
        new_rule.add_attribute("doesNotHaveTheWord", "Three")

        assert new_rule.final_rule_str == correct_rule

    def test_rule_with_email_addresses(self):
        """Test creating a rule that applies to a specified set of email addresses
        """
        correct_rule = "<!-- Mail Filter -->\n<entry>\n\t<category term='filter'></category>\n\t<title>Mail Filter</title>\n\t<content></content>\n\t<apps:property name='from' value='test1@test.com OR test2@test.com'/>\n\t<apps:property name='subject' value='Meow'/>\n\t<apps:property name='hasTheWord' value='Bla bla'/>\n\t<apps:property name='doesNotHaveTheWord' value='Three'/>\n\t<apps:property name='shouldNeverSpam' value='false'/>\n</entry>".expandtabs(_hp.TAB_SPACING)

        new_rule = Rule(list_of_emails=["test1@test.com", "test2@test.com"])
        new_rule.add_attribute("shouldNeverSpam", "false")
        new_rule.add_attribute("hasTheWord", "Bla bla")
        new_rule.add_attribute("subject", "Meow")
        new_rule.add_attribute("doesNotHaveTheWord", "Three")

        assert new_rule.final_rule_str == correct_rule

    def test_rule_with_multiple_labels(self):
        """Test whether a rule with multiple labels corretly builds
        """
        correct_rule = "<!-- START --- Mail Filter --- START -->\n<!-- Mail Filter (apple) -->\n<entry>\n\t<category term='filter'></category>\n\t<title>Mail Filter</title>\n\t<content></content>\n\t<apps:property name='label' value='apple'/>\n\t<apps:property name='from' value='test1@test.com OR test2@test.com'/>\n\t<apps:property name='subject' value='Meow'/>\n\t<apps:property name='hasTheWord' value='Bla bla'/>\n\t<apps:property name='doesNotHaveTheWord' value='Three'/>\n\t<apps:property name='shouldNeverSpam' value='false'/>\n</entry>\n<!-- Mail Filter (banana) -->\n<entry>\n\t<category term='filter'></category>\n\t<title>Mail Filter</title>\n\t<content></content>\n\t<apps:property name='label' value='banana'/>\n\t<apps:property name='from' value='test1@test.com OR test2@test.com'/>\n\t<apps:property name='subject' value='Meow'/>\n\t<apps:property name='hasTheWord' value='Bla bla'/>\n\t<apps:property name='doesNotHaveTheWord' value='Three'/>\n\t<apps:property name='shouldNeverSpam' value='false'/>\n</entry>\n<!-- Mail Filter (mango) -->\n<entry>\n\t<category term='filter'></category>\n\t<title>Mail Filter</title>\n\t<content></content>\n\t<apps:property name='label' value='mango'/>\n\t<apps:property name='from' value='test1@test.com OR test2@test.com'/>\n\t<apps:property name='subject' value='Meow'/>\n\t<apps:property name='hasTheWord' value='Bla bla'/>\n\t<apps:property name='doesNotHaveTheWord' value='Three'/>\n\t<apps:property name='shouldNeverSpam' value='false'/>\n</entry>\n<!-- END --- Mail Filter --- END -->".expandtabs(_hp.TAB_SPACING)

        new_rule = Rule(list_of_emails=["test1@test.com", "test2@test.com"])
        new_rule.add_attribute("label", ["apple", "banana", "mango"])
        new_rule.add_attribute("shouldNeverSpam", "false")
        new_rule.add_attribute("hasTheWord", "Bla bla")
        new_rule.add_attribute("subject", "Meow")
        new_rule.add_attribute("doesNotHaveTheWord", "Three")

        assert new_rule.final_rule_str == correct_rule
