
with open("input") as f:
    numbers = [int(n) for n in f.read().strip().split("\n")]

# print(numbers)

print("Puzzle 1")

def is_sum(number, preamble):
    for i, p1 in enumerate(preamble):
        p2 = number - p1
        if p2 in preamble[:i] + preamble[i+1:]:
            # print(p1, p2)
            return True
    return False



preamble_size = 25
preamble = numbers[:preamble_size]


for number in numbers[preamble_size:]:
    if not is_sum(number, preamble):
        print(number)
        invalid_number = number
        break
    preamble.pop(0)
    preamble.append(number)


print("Puzzle 2")
# def find_contiguous_set(invalid_number, preamble):
#     for i, p1 in enumerate(preamble):
#         contiguous_set = [p1]
#         rest = invalid_number - p1
#         # print("rest", rest)
#         if rest < 0:
#             continue
#         elif rest == 0:
#             return [p1]
#         else:
#             rest_numbers = find_contiguous_set(rest, preamble[:i] + preamble[i+1:])
#             print(rest_numbers)
#             if rest_numbers is not False:
#                 contiguous_set += rest_numbers
#                 print("contiguous_set", contiguous_set, invalid_number)
#                 if sum(contiguous_set) == invalid_number:
#                     return contiguous_set
#     return False

def find_contiguous_set(invalid_number, numbers):
    for i, n in enumerate(numbers):
        contiguous_set = []
        while True:
            contiguous_set.append(numbers[i])
            if sum(contiguous_set) == invalid_number:
                return contiguous_set
            if sum(contiguous_set) > invalid_number:
                break
            i += 1



numbers.remove(invalid_number)
contiguous_set = find_contiguous_set(invalid_number, numbers)
print(min(contiguous_set)+max(contiguous_set))