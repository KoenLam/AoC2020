import re

with open("input") as f:
    program = [l.split(" = ") for l in f.read().strip().split("\n")]


print("Puzzle 1")

def apply_mask(val, mask):
    val_bin = format(int(val), f'0>{len(mask)}b')
    after_mask = ""
    for v, m in zip(val_bin, mask):
        if m == "X":
            after_mask += v
        else:
            after_mask += m
    # print(after_mask, int(after_mask, 2))
    return int(after_mask, 2)


memory = dict()
mask = None
for var, val in program:
    if var == "mask":
        mask = val
    else:
        after_mask = apply_mask(val, mask)
        loc = re.findall("\d+", var)[0]
        memory[loc] = after_mask

# print(memory)
print(sum(memory.values()))

print("Puzzle 2")
def address_mask(val, mask):
    val_bin = format(int(val), f"0>{len(mask)}b")
    after_mask = ""
    for v, m in zip(val_bin, mask):
        if m == "0":
            after_mask += v
        else:
            after_mask += m
    # print(after_mask, int(after_mask, 2))
    return after_mask

def findall_idx(list, val):
    return [i for i, l in enumerate(list) if l == val]

memory = dict()
mask = None
for var, val in program:
    if var == "mask":
        mask = val
    else:
        loc = re.findall("\d+", var)[0]
        address = address_mask(loc, mask)
        idxs = findall_idx(address, "X")

        for i in range(2**len(idxs)):
            i_bin = format(i, f"0>{len(idxs)}b")
            assert len(i_bin) == len(idxs)
            address_cpy = list(address)
            for b, idx in zip(i_bin, idxs):
                address_cpy[idx] = b
            address_cpy = "".join(address_cpy)
            # print(address_cpy)
            memory[address_cpy] = int(val)

        # break
print(sum(memory.values()))

        