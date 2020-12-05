# Solved December 1th 2020
# Bruteforced due to small input


with open('input') as f:
    nums = [int(n) for n in f.read().split('\n') if n]



# Puzzle 1
print("Puzzle 1")
for a, num1 in enumerate(nums):
    for b, num2 in enumerate(nums):
        if a != b and num1 + num2 == 2020:
                print(num1, num2)
                print(num1*num2)


# Puzzle 2
print("Puzzle 2")
for a, num1 in enumerate(nums):
    for b, num2 in enumerate(nums):
        for c, num3 in enumerate(nums):
            if a != b != c and num1 + num2 + num3 == 2020:
                    print(num1, num2, num3)
                    print(num1*num2*num3)
