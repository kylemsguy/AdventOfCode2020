import itertools

class Rule:
    def __init__(self, rule_num):
        self.num = rule_num
        self.sub_rules = []
        self.literal = None
        self.valid_strs = []

    def __repr__(self):
        return f"Rule: {self.num} ({self.sub_rules if not self.literal else self.literal})"

    def get_valid_strs(self):
        if self.literal:
            return [self.literal]
        else: 
            return self.valid_strs

    def evaluate_msg(self, msg):
        return msg in self.valid_strs


def get_rule(the_map, rule_num):
    if not rule_num in the_map:
        the_map[rule_num] = Rule(rule_num)
    return the_map[rule_num]


def process_subrules(rule):
    if rule.literal:
        return [rule.literal]
    elif rule.sub_rules:
        for r in rule.sub_rules:
            parts_evaluated = []
            for sr in r:
                s = process_subrules(sr)
                parts_evaluated.append(s)
            combs = itertools.product(*parts_evaluated)
            for c in combs:
                rule.valid_strs.append(''.join(c))
    return rule.valid_strs


def get_valid_strs(rule):
    if rule.literal:
        yield rule.literal
    else:
        yield from rule.valid_strs
        sub_rules = rule.sub_rules
        for i, r in enumerate(sub_rules):
            parts_evaluated = []
            for sr in r:
                s = get_valid_strs(sr)
                parts_evaluated.append(list(s))
            combs = itertools.product(*parts_evaluated)
            for c in combs:
                valid_str = ''.join(c)
                rule.valid_strs.append(valid_str)
                yield valid_str
        rule.sub_rules = []


def check_valid(rule, msg):
    if rule.literal:
        return msg == rule.literal
    else:
        for s in get_valid_strs(rule):
            if s == msg:
                return True
        return False


if __name__ == "__main__":
    with open("rules.txt") as infile:
    # with open("rules_short.txt") as infile:
        raw = infile.read()

    rules_raw = [line for line in raw.split('\n') if line.strip()]

    with open("messages.txt") as infile:
        raw = infile.read()

    messages = [line for line in raw.split('\n') if line.strip()]

    num_rules_map = {}

    for line in rules_raw:
        rule_num, r_rule = line.split(': ')
        rule_num = int(rule_num)

        rule = get_rule(num_rules_map, rule_num)

        if r_rule.startswith('"'):
            rule.literal = r_rule.strip('"')
        else:
            r_sub_rules = r_rule.split(' | ')

            sub_rules = []
            for r in r_sub_rules:
                parts = r.split(' ')
                rule_parts = []
                for p in parts:
                    p = int(p)
                    rule_part = get_rule(num_rules_map, p)
                    rule_parts.append(rule_part)
                sub_rules.append(rule_parts)

            rule.sub_rules = sub_rules

    # process_subrules(num_rules_map[0])

    valid_msgs = 0
    rule_0 = num_rules_map[0]
    for i, msg in enumerate(messages):
        valid = check_valid(rule_0, msg)
        if valid:
            print(i, msg, "Valid")
            valid_msgs += valid
    print(valid_msgs)
