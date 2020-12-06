
with open("input", "r") as f:
    votes = f.read()[:-1].replace("\n", " ").split("  ")

# print(votes)

print("Puzzle 1")
counts = 0
for vote in votes:
    vote = vote.replace(" ", "")
    counts += len(set(vote))
print(counts)


print("Puzzle 2")
counts2 = 0
for vote in votes:
    vote = vote.split(" ")
    for answer in vote[0]:
        all_yes = True
        for answers in vote[1:]:
            if answer not in answers:
                all_yes = False
                break
            if not all_yes:
                break
        if all_yes:
            print(answer, vote)
            counts2 += 1
print(counts2)
    
            
