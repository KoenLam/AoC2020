
from os import error
from math import cos, pi, sin, sqrt


with open("input") as f:
    actions = f.read().strip().split("\n")


# print(actions)

print("Puzzle 1")

E, N, W, S = 0,1,2,3

cur_dir = E
pos = {"x":0, "y":0}

for action in actions:
    dir, val = action[0], int(action[1:])
    # print(action)
    if dir == "F":
        if cur_dir == E:
            pos["x"] += val
        elif cur_dir == W:
            pos["x"] -= val
        elif cur_dir == N:
            pos["y"] += val
        elif cur_dir == S:
            pos["y"] -= val
        else:
            raise error(f"Unknown Direction {cur_dir}")
    elif dir == "N":
        pos["y"] += val
    elif dir == "S":
        pos["y"] -= val
    elif dir == "E":
        pos["x"] += val
    elif dir == "W":
        pos["x"] -= val
    elif dir == "L":
        # print(cur_dir, action)
        cur_dir = (cur_dir + (val // 90)) % 4
        # print(cur_dir)
    elif dir == "R":
        cur_dir = (cur_dir + (-val // 90 )) % 4
    else:
        raise error("Unknown Action")

# print(pos)
man_dist = abs(pos["x"]) + abs(pos["y"])
print(man_dist)


print("\nPuzzle 2")

way_pos = {"x":10, "y":1}
ship_pos = {"x":0, "y":0}

for action in actions:
    dir, val = action[0], int(action[1:])
    # print(action, ship_pos)
    if dir == "F":
        ship_pos["x"] += val*way_pos["x"] 
        ship_pos["y"] += val*way_pos["y"]
    elif dir == "N":
        way_pos["y"] += val
    elif dir == "S":
        way_pos["y"] -= val
    elif dir == "E":
        way_pos["x"] += val
    elif dir == "W":
        way_pos["x"] -= val
    elif dir == "L":
        if val == 90:
            way_pos["x"], way_pos["y"] = -way_pos["y"], way_pos["x"]
        elif val == 180:
            way_pos["x"] *= -1
            way_pos["y"] *= -1
        elif val == 270:
            way_pos["x"], way_pos["y"] = way_pos["y"], -way_pos["x"]
        else:
            raise error(f"Unknown angle {action}")
    elif dir == "R":
        val = 360 - val
        if val == 90:
            way_pos["x"], way_pos["y"] = -way_pos["y"], way_pos["x"]
        elif val == 180:
            way_pos["x"] *= -1
            way_pos["y"] *= -1
        elif val == 270:
            way_pos["x"], way_pos["y"] = way_pos["y"], -way_pos["x"]
        else:
            raise error(f"Unknown angle {action}")
    else:
        raise error(f"Unknown Action {action}")

man_dist = abs(ship_pos["x"]) + abs(ship_pos["y"])
print(man_dist)



