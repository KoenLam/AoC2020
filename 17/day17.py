from collections import defaultdict
from itertools import product

import numpy as np

with open("input") as f:
    raw_map = f.read().strip().split("\n")


print("Puzzle 1")
# print(raw_map)
cubes = defaultdict(lambda: False)

# Parse map
for y, line in enumerate(raw_map):
    for x, val in enumerate(line):
        if val == "#":
            cubes[(x,y,0)] = True



def cycle(cubes):
    dd = [-1,0,1]
    new_cubes = cubes.copy()

    # Find x, y, z limits
    keys = list(cubes.keys())
    xb = max(map(lambda x: abs(x[0]), keys))+5
    yb = max(map(lambda x: abs(x[1]), keys))+5
    zb = max(map(lambda x: abs(x[2]), keys))+5

    # print(xb, yb, zb)
    # Simulate rules
    for x, y, z in product(range(-xb, xb), range(-yb, yb), range(-zb, zb)):
        active_neighbors = 0
        for dx, dy, dz in product(dd, dd, dd):
            if cubes[(x+dx, y+dy, z+dz)] and not (dx == 0 and dy == 0 and dz == 0):
                active_neighbors += 1

        # Cube is active
        if cubes[(x,y,z)]:
            if not(2 <= active_neighbors <= 3):
                new_cubes.pop((x,y,z))
        # Cube is inactive
        else:
            if active_neighbors == 3:
                new_cubes[(x,y,z)] = True
    return new_cubes
# print(map)

for _ in range(6):
    cubes = cycle(cubes)
print(len(cubes.keys()))
        


print("Puzzle 2")
# print(raw_map)
cubes4D = defaultdict(lambda: False)

# Parse map
for y, line in enumerate(raw_map):
    for x, val in enumerate(line):
        if val == "#":
            cubes4D[(x,y,0,0)] = True



def cycle4D(cubes):
    dd = [-1,0,1]
    new_cubes = cubes.copy()

    # Find x, y, z, w limits
    keys = list(cubes.keys())
    xb = max(map(lambda x: abs(x[0]), keys))+5
    yb = max(map(lambda x: abs(x[1]), keys))+5
    zb = max(map(lambda x: abs(x[2]), keys))+5
    wb = max(map(lambda x: abs(x[3]), keys))+5

    # Simulate rules
    for x, y, z, w in product(range(-xb, xb), range(-yb, yb), range(-zb, zb), range(-wb, wb)):
        active_neighbors = 0
        for dx, dy, dz, dw in product(dd, dd, dd, dd):
            if cubes[(x+dx, y+dy, z+dz, w+dw)] and not (dx == 0 and dy == 0 and dz == 0 and dw ==0):
                active_neighbors += 1

        # Cube is active
        if cubes[(x,y,z,w)]:
            if not(2 <= active_neighbors <= 3):
                new_cubes.pop((x,y,z,w))
        # Cube is inactive
        else:
            if active_neighbors == 3:
                new_cubes[(x,y,z,w)] = True
    return new_cubes
# print(map)

for _ in range(6):
    cubes4D = cycle4D(cubes4D)
print(len(cubes4D.keys()))
