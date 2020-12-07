import re

with open('input') as f:
    rules = [r.split("contain") for r in f.read().strip().replace(" bags", "").replace(" bag", "").split("\n")]


print("Puzzle 1")
bags = dict()

# Add Rules
for rule in rules:
    bags[rule[0].strip()] = []
    for bag in rule[1].replace(".", "").strip().split(","):
        if bag == "no other":
            bags[rule[0].strip()].append([0, "no other"])
        else:
            bags[rule[0].strip()].append([int(bag.split()[0]), ' '.join(bag.split()[1:])])

# print(bags)

# Substitute bags (Quantity code doesn't work, but it's not required by the puzzle)
has_changed = True
while has_changed:
    has_changed = False

    for bag in bags.copy():
        for inside_bag_tag in bags[bag].copy():
            quantity, inside_bag = inside_bag_tag
            if inside_bag in bags.keys() and not re.findall("shiny gold", inside_bag):
                has_changed = True
                double_inside_bags = bags[inside_bag].copy()
                # for i, _ in enumerate(double_inside_bags):
                #     double_inside_bags[i][0] *= quantity
                bags[bag].remove(inside_bag_tag)

                for double_inside_bag in double_inside_bags:
                    if double_inside_bag[1] not in map(lambda x: x[1], bags[bag]):
                        bags[bag].append(double_inside_bag)
                    else:
                        for i, (count, x_bag) in enumerate(bags[bag]):
                            if x_bag == double_inside_bag[1]:
                                # print("test")
                                # print(bags[bag][i][0], double_inside_bag[0])
                                
                                # bags[bag][i][0] += double_inside_bag[0]
                                pass


count = 0
for bag in bags:
    for inside_bag in bags[bag]:
        if re.findall("shiny gold", inside_bag[1]):
            count += 1
print(count)

print("Puzzle 2")
bags = dict()

# Add Rules
for rule in rules:
    bags[rule[0].strip()] = []
    for bag in rule[1].replace(".", "").strip().split(","):
        if bag == "no other":
            bags[rule[0].strip()].append([0, "no other"])
        else:
            bags[rule[0].strip()].append([int(bag.split()[0]), ' '.join(bag.split()[1:])])



def count_bags(bags_list, count=0):
    for bag_tag in bags_list:
        quantity, bag = bag_tag
        count += quantity
        if bag in bags.keys() and bag != "no other":
            count += quantity*count_bags(bags[bag])
    return count

bag_count = count_bags(bags['shiny gold'])
print(bag_count)
