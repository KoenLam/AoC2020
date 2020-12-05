# Read input
with open('input') as f:
    pwds = [line.split() for line in f.read().replace(":","").replace("-", " ").split("\n")][:-1]


print("Puzzle 1")
i = 0
for line in pwds:
    lb, ub, l, pwd = line
    num_l = pwd.count(l)
    if int(lb) <= int(num_l) <= int(ub):
        print(lb, ub, num_l,  l,pwd)
        i += 1

print(i)

print("Puzzle 2")
i = 0
for line in pwds:
    idx1, idx2, l, pwd = line
    idx1 = int(idx1) - 1
    idx2 = int(idx2) - 1
    if (pwd[idx1] == l) ^ (pwd[idx2] == l):
        print(idx1, idx2, l, pwd)
        i += 1
print(i)