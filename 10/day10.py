import numpy as np

with open("input") as f:
    jolts = [int(l) for l in f.read().strip().split('\n')]


print("Puzzle 1")
phone_jolts = max(jolts) + 3
jolts.append(phone_jolts)
jolts.append(0)
jolts.sort()
diff = list(np.diff(jolts))

print(diff)
print(diff.count(1), diff.count(3), diff.count(1)*diff.count(3))


print("\nPuzzle 2")
# print(jolts)

# Count the possible jumps
possible_jumps = []
for i, jolt in enumerate(jolts):
    possible_jumps.append([])
    sum = 0
    for j, jolt_diff in enumerate(diff[i:]):
        sum += jolt_diff
        if sum <= 3:
            possible_jumps[i].append(i+j+1)
        else:
            break
# print(possible_jumps)


# Go backwards and count the possible paths
possible_paths = [1 for _ in jolts]
for i in range(len(possible_paths)):
    i = len(possible_paths) - i -1
    jump = possible_jumps[i]
    if len(jump) > 0:
        paths = 0
        for j in jump:
            paths += possible_paths[j]
        possible_paths[i] = paths
print(possible_paths[0])

# Kind of brute force (took too long)
# def count_possibilities(jumps, index=0, count=0):
#     if jumps[index]:
#         jump = jumps[index]
#         print(jump)
#         for j in jump:
#             count += count_possibilities(jumps,j)
#         return count
#     else:
#         return count+1

# print(count_possibilities(possible_jumps))
