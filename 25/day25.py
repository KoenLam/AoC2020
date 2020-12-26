

with open("input") as f:
    card_pk, door_pk = [int(i) for i in f.read().strip().split("\n")]


print("Puzzle 1")
sn = 7

# Brute force to obtain loop size

def calc_loop_size(sn, pk):
    i = 1
    val = sn
    while val != pk:
        val = (val*sn) % 20201227
        i += 1
    return i, val

def encrypt(sn, loop_size):
    val = sn
    for _ in range(1,loop_size):
        val = (val*sn) % 20201227
    return val

card_loop_size, _ = calc_loop_size(sn, card_pk)
door_loop_size, _ = calc_loop_size(sn, door_pk)

ek_card = encrypt(door_pk, card_loop_size)
ek_door = encrypt(card_pk, door_loop_size)

assert ek_card == ek_door

print(ek_card)

