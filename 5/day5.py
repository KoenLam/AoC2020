

# Read file
with open("input") as f:
    seats = [s for s in f.read().split("\n") if s]

# print(seats)

print("Puzzle 1")
num_rows = 128
num_columns = 8

seat_ids = []

for seat in seats:
    row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(seat[7:].replace("R", "1").replace("L", "0"), 2)
    seat_id = 8*row + column
    # print(seat_id)
    seat_ids.append(seat_id)

    # break

print(max(seat_ids))

print("Puzzle 2")
seat_ids.sort()

for i in range(len(seat_ids)-1):
    diff = seat_ids[i+1]-seat_ids[i]
    if diff > 1:
        print(seat_ids[i+1], seat_ids[i])
