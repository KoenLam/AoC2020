

filename = "input"
def get_input(filename):
    with open(filename) as f:
        player1, player2 = [c.split("\n")[1:] for c in f.read().strip().split("\n\n")]

    player1 = [int(c) for c in player1]
    player2 = [int(c) for c in player2]
    return player1, player2

print("Puzzle 1")
player1, player2 = get_input(filename)

while min(len(player1), len(player2)) > 0:
    p1 = player1.pop(0)
    p2 = player2.pop(0)

    assert p1 != p2

    if p1 > p2:
        player1.append(p1)
        player1.append(p2)
    elif p2 > p1:
        player2.append(p2)
        player2.append(p1)

winner = player1 + player2

score = 0
for i, val in enumerate(winner[::-1]):
    score += (i+1)*val

print(score)

print("Puzzle 2")
player1, player2 = get_input(filename)

def play_game(player1, player2):
    game_states = []

    while min(len(player1), len(player2)) > 0:
        if (player1, player2) in game_states:
            return 1, player1
        game_states.append((player1.copy(), player2.copy()))

        p1 = player1.pop(0)
        p2 = player2.pop(0)

        assert p1 != p2

        if len(player1) >= p1 and len(player2) >= p2:
            winner, _  = play_game(player1[:p1], player2[:p2])
        else:
            winner = 1 if p1 > p2 else 2

        assert winner in [1,2]
        if winner == 1:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)
    return (1, player1) if player1 else (2, player2)

_, winner  = play_game(player1, player2)

score = 0
for i, val in enumerate(winner[::-1]):
    score += (i+1)*val
print(score)