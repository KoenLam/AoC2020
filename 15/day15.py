

with open("input") as f:
    numbers = [int(l) for l in f.read().split(",")]


print("Puzzle 1")
target_number = 2020

numbers = numbers[::-1]
while len(numbers) != target_number:
    # print(len(numbers))
    prev_num = numbers[0]
    if prev_num not in numbers[1:]:
        numbers = [0] + numbers
    else:
        numbers = [numbers[1:].index(prev_num)+1] + numbers
print(numbers[0])

print("Puzzle 2")
with open("input") as f:
    numbers = [int(l) for l in f.read().split(",")]

nums = dict()
nums[0] = []
target = 30000000
for i, n in enumerate(numbers):
    nums[n] = [i+1]

i += 2 # To compensate for index starting at 0 instead of 1
prev = n
while i <= target:
    # print(i)
    # Prev num not first time
    if len(nums[prev]) > 1:
        prev = i - nums[prev][-2]-1
        if prev not in nums.keys():
            nums[prev] = []
        nums[prev].append(i)
    else:
        nums[0].append(i)
        prev = 0
    i += 1

print(prev)



