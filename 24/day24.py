from collections import defaultdict

import numpy as np

with open("input") as f:
    flips = f.read().strip().split()


print("Puzzle 1")


def split_flips(flips):
    for i, flip in enumerate(flips):
        f = []
        dir = ""
        for l in flip:
            dir += l  # e, se, sw, w, nw, and ne
            if dir in ["e", "se", "sw", "w", "nw", "ne"]:
                f.append(dir)
                dir = ""
        flips[i] = f
    return flips


flips = split_flips(flips)
tiles_flipped = defaultdict(lambda: False)


dir2coords = dict()
dir2coords["e"] = np.array([0, 1])
dir2coords["se"] = np.array([1, 0.5])
dir2coords["sw"] = np.array([1, -0.5])
dir2coords["w"] = np.array([0, -1])
dir2coords["nw"] = np.array([-1, -0.5])
dir2coords["ne"] = np.array([-1, 0.5])

for flip in flips:
    coords = np.array([0, 0], dtype=float)
    for dir in flip:
        coords += dir2coords[dir]
    tiles_flipped[tuple(coords)] ^= True


def count_black_tiles(x): return list(x.values()).count(True)


print(count_black_tiles(tiles_flipped))


print("Puzzle 2")


def gen_adjacent_coords(tile_coords):
    return [(tile_coords[0]+dy, tile_coords[1]+dx) for dy, dx in dir2coords.values()]


def flip_tiles(tiles_flipped):
    new_tiles_flipped = tiles_flipped.copy()

    # Generate tiles to check
    tile_coords = list(tiles_flipped.keys())
    for tile_coord in list(tiles_flipped.keys()):
        tile_coords += gen_adjacent_coords(tile_coord)
    tile_coords = set(tile_coords)

    # Count adjacent black tiles
    for tile_coords in tile_coords:
        num_black_tiles = 0
        for adjacent_tile_coords in gen_adjacent_coords(tile_coords):
            if tiles_flipped[adjacent_tile_coords]:
                num_black_tiles += 1

        # Black tile
        if tiles_flipped[tile_coords] \
                and (num_black_tiles == 0 or num_black_tiles > 2):
            new_tiles_flipped[tile_coords] = False
        # White tile
        elif not tiles_flipped[tile_coords] \
                and num_black_tiles == 2:
            new_tiles_flipped[tile_coords] = True
    return new_tiles_flipped


for _ in range(100):
    tiles_flipped = flip_tiles(tiles_flipped)
print(count_black_tiles(tiles_flipped))
