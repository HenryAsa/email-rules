import pytest

import gmail_rules.actions as action
from gmail_rules.actions.rule_collection import Rule_Collection
import gmail_rules.rules as _R
import gmail_rules.utils.helpers as _hp

class TestRuleCollection:

    collection_1 : Rule_Collection = None
    rule_1 = _R.Copy_To("rule_1", ["1"])

    def test_rule_collection_definition(self) -> None:
        """Test defining a new rule_collection
        """
        self.collection_1 = action.Rule_Collection()
        assert isinstance(self.collection_1, Rule_Collection)

    collection_1 : Rule_Collection = action.Rule_Collection()

    def test_add_rule_to_rule_collection(self) -> None:
        """Test adding a rule to the collection
        """
        ## ADD RULE TO RULE_COLLECTION ##
        self.collection_1.add_rule(self.rule_1)

        ## CORRECT RULE STRING ##
        rule_1_str_1 = "<!-- COPY TO: rule_1 -->\n<entry>\n\t<category term='filter'></category>\n\t<title>COPY TO: rule_1</title>\n\t<content></content>\n\t<apps:property name='label' value='rule_1'/>\n\t<apps:property name='from' value='1'/>\n\t<apps:property name='shouldNeverSpam' value='true'/>\n</entry>".expandtabs(_hp.TAB_SPACING)

        assert self.collection_1[self.rule_1.name] is self.rule_1
        assert self.collection_1[self.rule_1.name].final_rule_str == rule_1_str_1

    def test_update_rule_in_collection(self) -> None:
        """Test modifying a rule and how that changes in the collection
        """
        ## MODIFY RULE ##
        self.rule_1.add_attribute("subject", "233")

        ## CORRECT RULE STRING ##
        rule_1_str_2 = "<!-- COPY TO: rule_1 -->\n<entry>\n\t<category term='filter'></category>\n\t<title>COPY TO: rule_1</title>\n\t<content></content>\n\t<apps:property name='label' value='rule_1'/>\n\t<apps:property name='from' value='1'/>\n\t<apps:property name='subject' value='233'/>\n\t<apps:property name='shouldNeverSpam' value='true'/>\n</entry>".expandtabs(_hp.TAB_SPACING)

        assert self.collection_1[self.rule_1.name] is self.rule_1
        assert self.collection_1[self.rule_1.name].final_rule_str == rule_1_str_2

    def test_add_another_rule_to_rule_collection(self):
        """Test having more than one rule in a collection
        """
        ## ADD RULE_2
        rule_2 = _R.Copy_To("rule_2", ["Beijing", "Shanghai"])
        self.collection_1.add_rule(rule_2)

        ## CORRECT RULE_2 STRING ##
        rule_2_str = "<!-- COPY TO: rule_2 -->\n<entry>\n\t<category term='filter'></category>\n\t<title>COPY TO: rule_2</title>\n\t<content></content>\n\t<apps:property name='label' value='rule_2'/>\n\t<apps:property name='from' value='Beijing OR Shanghai'/>\n\t<apps:property name='shouldNeverSpam' value='true'/>\n</entry>".expandtabs(_hp.TAB_SPACING)

        assert self.collection_1[rule_2.name] is rule_2
        assert self.collection_1[rule_2.name].final_rule_str == rule_2_str
    
    def test_add_rule_with_same_name_to_collection(self):
        """Ensure a KeyError is raised when rules with the same name are added to a collection
        """
        rule_1 = _R.Rule(rule_name="Duplicate Rule", rule_defaults={"subject": "This can be added to the collection"})
        rule_2 = _R.Rule(rule_name="Duplicate Rule", rule_defaults={"subject": "This should not be added"})

        self.collection_1.add_rule(rule_1)
        with pytest.raises(KeyError):
            self.collection_1.add_rule(rule_2)

    def test_adding_multiple_rules_to_collection(self):
        """Test adding multiple rules to the collection at once
        """
        new_rule_1 = _R.Rule(["mango@gmail.com"], rule_name="Testing")
        new_rule_1.add_attribute("subject", "[IMPORTANT] Mangos for Sale")
        new_rule_2 = _R.Copy_To("fruits", ["banana@gmail.com", "kiwi@gmail.com"])
        new_rule_2.add_attribute("subject", "FRUIT")

        self.collection_1.add_rules([new_rule_1, new_rule_2])

        assert new_rule_1 in self.collection_1.rules_dict.values()
        assert new_rule_2 in self.collection_1.rules_dict.values()

    def test_adding_multiple_rules_error_raised(self):
        """Test adding multiple rules to the collection but one of the rules should raise an error
        """
        new_rule_1 = _R.Rule(["mangos@gmail.com"], rule_name="Testing Again")
        new_rule_1.add_attribute("subject", "[IMPORTANT] Mangos for Sale")
        new_rule_2 = _R.Copy_To("more fruits", ["bananas@gmail.com", "kiwi@gmail.com"])
        new_rule_2.add_attribute("subject", "FRUIT")

        not_a_rule = "cheese"

        with pytest.raises(TypeError):
            self.collection_1.add_rules([new_rule_1, new_rule_2, not_a_rule])
