
import sys
sys.path.append("../gmail-rules")

import gmail_rules.rules as rules
import gmail_rules.utils.helpers as hp

new_rule = rules.Copy_To("mango", ["test1", "test2"])
new_rule.add_attribute("hasTheWord", "Bla bla")
# new_rule.add_attribute("shouldNeverSpam", "false")
new_rule.add_attribute("doesNotHaveTheWord", "Three")
new_rule.add_attribute("doesNotHaveTheWordMANGO", "Three", True)
new_rule.add_attribute("subject", "Meow")
print(new_rule.final_rule_str)
# new_rule.
