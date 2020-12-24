import re

with open("input") as f:
    raw_rules, raw_messages = f.read().strip().split("\n\n")


print("Puzzle 1")
def parse_rules(raw_rules):
    rules = dict()
    for rule in raw_rules.split("\n"):
        key, val = rule.split(":")
        val = val.strip().replace('"','')
        if re.findall("\|", val):
            val = f"( {val} )"
        rules[key.strip()] = val
    return rules

def parse_message(raw_messages):
    return raw_messages.split("\n")

def substitute_rules(rules, part2=False):
    changed = True
    while changed:
        changed = False
        for rule in rules:
            rule_new = []
            for subrule in rules[rule].split():
                if re.findall("\d", subrule) and (subrule != "11" or not part2):
                    # print("TEST", subrule, rules[subrule])
                    rule_new.append(rules[subrule])
                    changed = True
                else:
                    rule_new.append(subrule)
            rules[rule] = " ".join(rule_new)
        # changed = False
    return rules

rules = parse_rules(raw_rules)
messages = parse_message(raw_messages)
rules = substitute_rules(rules)
count = 0
for message in messages:
    if re.fullmatch(rules['0'].replace(" ", ""), message):
        count += 1
print(count)

print("Puzzle 2")
def aoc_match(rules, message):
    # Hardcoded to match 0: 8 11
    r8 = rules['8'].replace(" ", "")
    r42 = rules['42'].replace(" ", "")
    r31 = rules['31'].replace(" ", "")

    i = 1
    while True:
        m8 = re.match(f"{r8}{{{i}}}", message)
        if m8:
            m8_len = len(m8.group(0))

            j = 1
            while True:
                m42 = re.match(f"{r42}{{{j}}}", message[m8_len:])
                if m42:
                    m42_len = len(m42.group(0))
                    if re.fullmatch(f"{r31}{{{j}}}", message[m8_len+m42_len:]):
                        return True
                else:
                    break
                j += 1
        else:
            break
        i += 1

    return False

rules = parse_rules(raw_rules)
rules = substitute_rules(rules, part2=True)
count = 0
for message in messages:
    if aoc_match(rules, message):
        count += 1
print(count)