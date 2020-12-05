
# Read file
with open('input') as f:
    map = [m for m in f.read().split("\n") if m]

print('Puzzle 1')
start = 0
encounters = []
for m in map:
    encounters.append(m[start])
    start = (start + 3) % len(m)

print(encounters.count("#"))


print('Puzzle 2')

def count_trees(map, right, down=1):
    start = 0
    encounters = []
    for i in range(0,len(map), down):
        m = map[i]
        encounters.append(m[start])
        start = (start + right) % len(m)
    return encounters.count("#")


result = count_trees(map, 1, 1) * count_trees(map, 3, 1) * count_trees(map, 5, 1) * count_trees(map, 7, 1) * count_trees(map, 1, 2)    

print(result)