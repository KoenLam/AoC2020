 

from itertools import product

import numpy as np


with open("input") as f:
    map = np.array([list(r) for r in f.read().strip().split("\n")])



def in_bounds(x,y, shape):
    height, width = shape

    if x < 0 or x >= width:
        # print("Not x")
        return False
    
    if y < 0 or y >= height:
        # print("Not y", y, height)
        return False

    return True

def count_adjacent_seats(map, x, y):
    dx = [-1,0,1]
    dy = [-1,0,1]
    num_occupied_seats = 0
    for dxx, dyy in product(dx, dy):
        # print(y, dyy, x, dxx)
        xn = x + dxx
        yn = y + dyy

        if (dxx == 0 and dyy == 0) or not in_bounds(xn, yn, map.shape):
            # print(xn, yn, "not")
            continue
        if map[y+dyy, x+dxx] == "#":
            # print(y, dyy, x, dxx, map[y+dyy, x+dxx])
            num_occupied_seats += 1
    return num_occupied_seats


def print_map(map):
    for m in map:
        print(''.join(m))

def round_map(map):
    new_map = map.copy()

    for y, r in enumerate(map):
        for x, pos in enumerate(r):
            if pos == "L":
                if count_adjacent_seats(map, x, y) == 0:
                    # print(y,x)
                    new_map[y,x] = "#"
            elif pos == "#" and count_adjacent_seats(map, x, y) >= 4:
                    new_map[y,x] = "L"
    return new_map

def count_seats(map):
    seats = sum([list(r).count("#") for r in map])
    return seats


def walk_map(map, x, y, dx, dy):

    nx = x + dx
    ny = y + dy

    if not in_bounds(nx, ny, map.shape):
        return "."
    elif map[ny, nx] == ".":
        return walk_map(map, nx, ny, dx, dy)
    else:
        return map[ny, nx]


def count_adjacent_seats2(map, x, y):
    dx = [-1,0,1]
    dy = [-1,0,1]

    num_occupied_seats = 0
    for dxx, dyy in product(dx, dy):
        # if dxx != 0 or dyy != 0:
        #     print("testing", x, y, dxx, dyy, num_occupied_seats, walk_map(map, x,y, dxx, dyy))
        if (dxx == 0 and dyy == 0):
            # print(xn, yn, "not")
            continue
        elif walk_map(map, x,y, dxx, dyy) == "#":
            # print(y, dyy, x, dxx, map[y+dyy, x+dxx])
            num_occupied_seats += 1
    # print("NUM SEATS", num_occupied_seats)
    return num_occupied_seats


def round_map2(map):
    new_map = map.copy()

    for y, r in enumerate(map):
        for x, pos in enumerate(r):
            if pos == "L":
                if count_adjacent_seats2(map, x, y) == 0:
                    # print(y,x)
                    new_map[y,x] = "#"
            elif pos == "#":
                if count_adjacent_seats2(map, x, y) >= 5:
                    new_map[y,x] = "L"
    return new_map


print("Puzzle 1")
old = map.copy()
r = round_map(map)
while not np.array_equal(r, old):
    old = r
    r = round_map(r)
# print_map(r)
print(count_seats(r))

print("Puzzle 2")

old = map
r = round_map2(map)
while not np.array_equal(r, old):
    old = r
    r = round_map2(r)

# print_map(r)
print(count_seats(r))


