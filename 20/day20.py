import numpy as np
from collections import defaultdict
from functools import reduce


with open("input") as f:
    raw_tiles = f.read().strip().split("\n\n")


print("Puzzle 1")
def parse_tiles(raw_tiles):
    tiles = {}
    for raw_tile in raw_tiles:
        title, tile = raw_tile.split(":\n")

        # Remove Tile word
        title = int(title.strip("Tile"))
        
        # Replace and make np array
        tile = tile.replace("#", "1").replace(".", "0")
        tile = np.array([list(t) for t in tile.split("\n")], dtype=int)

        tiles[title] = tile

    return tiles


def is_image_pair(tile1, tile2):
    if np.array_equal(tile1[:,-1], tile2[:,0]):
        return "e"
    elif np.array_equal(tile1[:,0], tile2[:,-1]):
        return "w"
    elif np.array_equal(tile1[-1,:], tile2[0,:]):
        return "s"
    elif np.array_equal(tile1[0,:], tile2[-1,:]):
        return "n"
    return None




tiles = parse_tiles(raw_tiles)
# print(len(tiles))

tiles_fit = defaultdict(set)
for tile_id1 in tiles.keys():
    for tile_id2 in tiles.keys():
        if tile_id1 != tile_id2:
            # Normal
            if side := is_image_pair(tiles[tile_id1], tiles[tile_id2]):
                # print(tile_id1, tile_id2, "Normal")
                tiles_fit[tile_id1].add((side, tile_id2))
            
            # Rotate 90
            tile2_rot90 = np.rot90(tiles[tile_id2])
            if side := is_image_pair(tiles[tile_id1], tile2_rot90):
                # print(tile_id1, tile_id2, "Rotate 90")
                tiles_fit[tile_id1].add((side, tile_id2))

            # Rotate 180
            tile2_rot180 = np.rot90(np.rot90(tiles[tile_id2]))
            if side := is_image_pair(tiles[tile_id1], tile2_rot180):
                # print(tile_id1, tile_id2, "Rotate 180")
                tiles_fit[tile_id1].add((side, tile_id2))

            # Rotate 270
            tile2_rot270 = np.rot90(np.rot90(np.rot90(tiles[tile_id2])))
            if side := is_image_pair(tiles[tile_id1], tile2_rot270):
                # print(tile_id1, tile_id2, "Rotate 270")
                tiles_fit[tile_id1].add((side, tile_id2))

            # Flip lr
            tile2_flip_lr = np.fliplr(tiles[tile_id2])
            if side := is_image_pair(tiles[tile_id1], tile2_flip_lr):
                # print(tile_id1, tile_id2, "Flip lr")
                tiles_fit[tile_id1].add((side, tile_id2))

            # Rotate 90 + Flip lr
            tile2_rot90flip_lr = np.fliplr(tile2_rot90)
            if side := is_image_pair(tiles[tile_id1], tile2_rot90flip_lr):
                # print(tile_id1, tile_id2, "Rotate 90 + flip lr")
                tiles_fit[tile_id1].add((side, tile_id2))

            
            # Rotate 180 + Flip lr
            tile2_rot180flip_lr = np.fliplr(tile2_rot180)
            if side := is_image_pair(tiles[tile_id1], tile2_rot180flip_lr):
                # print(tile_id1, tile_id2, "Rotate 180 + flip lr")
                tiles_fit[tile_id1].add((side, tile_id2))

            # Rotate 270 + Flip lr
            tile2_rot270flip_lr = np.fliplr(tile2_rot270)
            if side := is_image_pair(tiles[tile_id1], tile2_rot270flip_lr):
                # print(tile_id1, tile_id2, "Rotate 270 + flip lr")
                tiles_fit[tile_id1].add((side, tile_id2))

            # Flip ud
            tile2_flip_ud = np.flipud(tiles[tile_id2])
            if side := is_image_pair(tiles[tile_id1], tile2_flip_ud):
                # print(tile_id1, tile_id2, "Flip ud")
                tiles_fit[tile_id1].add((side, tile_id2))

            # Rotate 90 + Flip ud
            tile2_rot90flip_ud = np.flipud(tile2_rot90)
            if side := is_image_pair(tiles[tile_id1], tile2_rot90flip_ud):
                # print(tile_id1, tile_id2, "Rotate 90 + flip ud")
                tiles_fit[tile_id1].add((side, tile_id2))

            
            # Rotate 180 + Flip ud
            tile2_rot180flip_ud = np.flipud(tile2_rot180)
            if side := is_image_pair(tiles[tile_id1], tile2_rot180flip_ud):
                # print(tile_id1, tile_id2, "Rotate 180 + flip ud")
                tiles_fit[tile_id1].add((side, tile_id2))

            # Rotate 270 + Flip ud
            tile2_rot270flip_ud = np.flipud(tile2_rot180)
            if side := is_image_pair(tiles[tile_id1], tile2_rot270flip_ud):
                # print(tile_id1, tile_id2, "Rotate 270 + flip ud")
                tiles_fit[tile_id1].add((side, tile_id2))


corners = []
# print(tiles_fit)
for tile_id in tiles_fit.keys():
    if len(tiles_fit[tile_id]) == 2:
        print(tile_id, tiles_fit[tile_id])
        corners.append(tile_id)
# print(corners)
print(reduce(lambda a, b: a*b, corners))

print("Puzzle 2")

def decode_orientation(orientation):
    if orientation == "e":
        return (0,1)
    elif orientation == "n":
        return (-1,0)
    elif orientation == "w":
        return (0,-1)
    elif orientation == "s":
        return (1,0)
    return (0,0)

map_ids= np.zeros((int(np.sqrt(len(raw_tiles))), int(np.sqrt(len(raw_tiles)))), dtype=int)
# Note manual input required
map_ids[0,0] = 3847
map_ids[0,-1] = 3187

for y in range(len(map_ids[:,0])):
    for x in range(len(map_ids[0,:])-1):
        tile_id1 = map_ids[y,x]
        for tile_id2 in tiles.keys():
            if tile_id1 != tile_id2:
                
                trans_tiles = [
                    tiles[tile_id2],
                    np.rot90(tiles[tile_id2]),
                    np.rot90(np.rot90(tiles[tile_id2])),
                    np.rot90(np.rot90(np.rot90(tiles[tile_id2]))),
                    np.fliplr(tiles[tile_id2]),
                    np.fliplr(np.rot90(tiles[tile_id2])),
                    np.fliplr(np.rot90(np.rot90(tiles[tile_id2]))),
                    np.fliplr(np.rot90(np.rot90(np.rot90(tiles[tile_id2])))),
                    np.flipud(tiles[tile_id2]),
                    np.flipud(np.rot90(tiles[tile_id2])),
                    np.flipud(np.rot90(np.rot90(tiles[tile_id2]))),
                    np.flipud(np.rot90(np.rot90(np.rot90(tiles[tile_id2]))))
                    ]
                
                for trans_tile in trans_tiles:
                    if side := is_image_pair(tiles[tile_id1], trans_tile):
                        dy, dx = decode_orientation(side)
                        if map_ids[y+dy,x+dx] != 0:
                            assert map_ids[y+dy,x+dx] == tile_id2
                        else:
                            map_ids[y+dy, x+dx] = tile_id2
                            tiles[tile_id2] = trans_tile

print(map_ids)

# Verify image is correct
for y in range(0,len(map_ids[:,0])):
    for x in range(0,len(map_ids[0,:])):
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            # print(dx, dy, x, y, map_ids[y,x], map_ids[y+dy, x+dx])

            if 0 <= x+dx < len(map_ids[0,:]) and 0 <= y+dy < len(map_ids[:,0]):
                # print(map_ids[y,x], map_ids[y+dy,x+dx])
                assert (dy, dx) == decode_orientation(is_image_pair(tiles[map_ids[y,x]], tiles[map_ids[y+dy,x+dx]]))

# Remove borders
for tile_id in tiles.keys():
    tiles[tile_id] = tiles[tile_id][1:-1,1:-1]

# Construct image
image = []
for y in range(len(map_ids[:,0])):
    row = []
    for x in range(len(map_ids[0,:])):
        row.append(tiles[map_ids[y,x]])
    row = np.concatenate(row, axis=1)
    image.append(row)
image = np.concatenate(image, axis=0)

# Parse seamonster
seamonster = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
'''.replace(" ", "0").replace("#", "1").split("\n")[1:-1]
seamonster = np.array([list(t) for t in seamonster], dtype=int)
num_seamonster_parts = sum(sum(seamonster))
monster_y, monster_x = seamonster.shape

# Find seamonster
images = [
    image,
    np.rot90(image),
    np.rot90(np.rot90(image)),
    np.rot90(np.rot90(np.rot90(image))),
    np.fliplr(image),
    np.fliplr(np.rot90(image)),
    np.fliplr(np.rot90(np.rot90(image))),
    np.fliplr(np.rot90(np.rot90(np.rot90(image)))),
    np.flipud(image),
    np.flipud(np.rot90(image)),
    np.flipud(np.rot90(np.rot90(image))),
    np.flipud(np.rot90(np.rot90(np.rot90(image))))
    ]

for i,img in enumerate(images):
    num_seamonsters = 0

    for y in range(0,len(img[:,0])-monster_y):
        for x in range(0,len(img[0,:])-monster_x):
            # print(sum(sum(np.logical_and(img[y:y+monster_y,x:x+monster_x], seamonster))))
            if sum(sum(np.logical_and(img[y:y+monster_y,x:x+monster_x], seamonster))) == num_seamonster_parts:
                num_seamonsters += 1

            
    if num_seamonsters != 0:
        break

def print_image(image):
    for line in image:
        print("\n",end="")
        for val in line:
            char = "#" if val else "."
            print(char, end="")
    print()


water_roughness = sum(sum(image)) - num_seamonsters*num_seamonster_parts
# print(num_seamonsters)
print(water_roughness)

