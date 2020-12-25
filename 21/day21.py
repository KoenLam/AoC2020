from collections import defaultdict, Counter


with open("input") as f:
    raw_ingredients_list = f.read().strip().replace("(","").replace(")","").split("\n")

print("Puzzle 1")
def parse_ingredients_list(raw_ingredients_list):
    all_ingredients = []
    allergens = defaultdict(lambda :"")

    for line in raw_ingredients_list:
        ingredient, allergen = line.split("contains")
        for all in allergen.split(","):
            allergens[all.strip()] += ingredient
        all_ingredients += ingredient.split()
    
    for allergen in allergens:
        allergens[allergen] = Counter(allergens[allergen].split())

    return allergens, all_ingredients


allergens, all_ingredients = parse_ingredients_list(raw_ingredients_list)
# print(allergens)

allergens_map = defaultdict(list)
for allergen in allergens:
    max_val = max(allergens[allergen].values())
    for ingredient in allergens[allergen]:
        val = allergens[allergen][ingredient]
        
        if val == max_val:
            allergens_map[allergen].append(ingredient)


flatten = lambda l: [ss for s in l for ss in s]
# print(allergens_map)

# Assign each allergen one ingredient
changed = True
while changed:
    changed = False
    for allergen in allergens_map:
        if len(allergens_map[allergen]) > 1:
            for ingredient in allergens_map[allergen][::-1]: # Reversed to remove the least common ingredient first
                # print(allergen, ingredient, flatten(list(allergens_map.values())))
                if flatten(list(allergens_map.values())).count(ingredient) > 1 and len(allergens_map[allergen]) > 1:
                    allergens_map[allergen].remove(ingredient)
                    changed = True
                    break

ingredient_no_al = []
count = 0
for ingredient in set(all_ingredients):
    if ingredient not in flatten(list(allergens_map.values())):
        ingredient_no_al.append(ingredient)
        count += all_ingredients.count(ingredient)


# print(allergens_map)
print(count)

print("Puzzle 2")
for allergen in sorted(allergens_map):
    print(allergens_map[allergen][0], end=",", sep="")
print()

