

# raw_cups = list("389125467") # Example
raw_cups = list("327465189")  # My input
raw_cups = [int(c) for c in raw_cups]


print("Puzzle 1")


def _cycle(val, max):
    return val % max


def play_game(cups, iter=100):
    max_cup = max(cups)
    curr_idx = 0
    for i in range(iter):
        # print(i, cups[:20])
        # print(cups)
        curr_cup = cups[curr_idx]

        # Calculate pick up cups
        pick_up_idx = [_cycle(curr_idx+i, len(cups)) for i in range(1, 4)]
        pick_up_cups = []
        for idx in pick_up_idx:
            pick_up_cups.append(cups[idx])

        # Remove pick up cups
        cups = [cup for i, cup in enumerate(cups) if i not in pick_up_idx]

        dest_cup = _cycle(curr_cup-1-1, max_cup)+1
        while dest_cup in pick_up_cups:
            dest_cup = _cycle(dest_cup - 1-1, max_cup)+1
        dest_idx = cups.index(dest_cup)

        cups = cups[:dest_idx+1] + pick_up_cups + cups[dest_idx+1:]
        curr_idx = _cycle(cups.index(curr_cup)+1, len(cups))
    return cups


cups = raw_cups
cups = play_game(cups)

answer = []
start_idx = cups.index(1)
for i, _ in enumerate(cups):
    i = _cycle(start_idx+i, len(cups))
    answer.append(cups[i])

answer = "".join([str(a) for a in answer])
print(answer[1:])

print("Puzzle 2")
def play_game2(cups, iter=100):
    max_cup = max(cups)
    cups_dict = dict(zip(cups, cups[1:]))
    cups_dict[max_cup] = cups[0]

    curr_cup = cups[0]

    for i in range(iter):
        # print(i, curr_cup)
        # Calculate pick up cup
        pick_up_cups = [cups_dict[curr_cup]]
        for _ in range(2):
            pick_up_cups.append(cups_dict[pick_up_cups[-1]])

        # Find destination cup
        dest_cup = curr_cup - 1 if curr_cup - 1 else max_cup
        while dest_cup in pick_up_cups:
            dest_cup = dest_cup - 1 if dest_cup - 1 else max_cup

        cups_dict[curr_cup] = cups_dict[pick_up_cups[-1]]
        cups_dict[pick_up_cups[-1]] = cups_dict[dest_cup]
        cups_dict[dest_cup] = pick_up_cups[0]

        curr_cup = cups_dict[curr_cup]
    return cups_dict


cups = raw_cups
start_cup = max(cups)
while len(cups) < 1000000:
    start_cup += 1
    cups.append(start_cup)

cups_dict = play_game2(cups, 10000000)
next1 = cups_dict[1]
next2 = cups_dict[next1]

# print(next1, next2)
print(next1*next2)
