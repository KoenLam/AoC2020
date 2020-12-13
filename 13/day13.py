from math import gcd
from functools import reduce

with open("input") as f:
    lines = f.read().strip().split()
    timestamp  = int(lines[0])
    busIDs = [int(n) for n in lines[1].split(",") if n != "x"]


# print(timestamp)
# print(busIDs)


print("Puzzle 1")
div = [n - timestamp % n for n in busIDs]
earliest_bus = busIDs[div.index(min(div))]
print(earliest_bus*min(div))


print("Puzzle 2")
offsets = [lines[1].split(",").index(str(busID)) for busID in busIDs]
# print(busIDs)
# print(offsets)

def lcm(a, b):
    return a*b // gcd(a,b)

timestamps = []
for busID, offset in zip(busIDs[1:], offsets[1:]):
    i = 0
    while i < busIDs[0]*busID:
        if i % busIDs[0] == 0 and ((i+offset) % busID) == 0:
            timestamps.append(i)
            break
        i += 1


M = reduce(lambda a,b: a*b, busIDs)

x = 0
for i in range(len(timestamps)):
    mi = busIDs[i+1]
    Mi = M // mi
    # print(Mi, mi)
    yi = pow(Mi,-1,mi)
    x += timestamps[i]*Mi*yi
print(x%M)

