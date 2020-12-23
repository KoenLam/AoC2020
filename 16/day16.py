import re

import numpy as np

with open("input") as f:
    ranges, my_ticket, nearby_tickets = f.read().strip().split("\n\n")

print("Puzzle 1")
def parse_ranges(ranges):
    range_dict = dict()
    for l in ranges.split("\n"):
        field, range = l.split(": ")
        range = range.split("or")
        range_dict[field] = [r.strip() for r in range]

    return range_dict

def parse_tickets(tickets):
    return [t.split(",") for t in tickets.split("\n")[1:]]


def in_range(range, number):
    lb, ub = range.split("-")
    if int(lb) <= int(number) <= int(ub):
        return True
    return False

flatten = lambda l: [item for sublist in l for item in sublist]

ranges_dict = parse_ranges(ranges)
my_ticket = parse_tickets(my_ticket)[0]
nearby_tickets = parse_tickets(nearby_tickets)
valid_tickets = []

error_rate = 0
for ticket in nearby_tickets:
    valid_ticket = True
    for val in ticket:
        valid = False
        for pattern in flatten(ranges_dict.values()):
            if in_range(pattern, val):
               valid = True
               break
        if not valid: 
            error_rate += int(val)
            # print(val)
            valid_ticket = False
    if valid_ticket:
        valid_tickets.append(ticket)
    
print(error_rate)

print("Puzzle 2")
def is_valid_field(ranges, numbers):
    range1, range2 = ranges
    for number in numbers:
        if not(in_range(range1, number) or in_range(range2, number)):
            return False
    return True

# Check possible position of fields
valid_ticket_mat = np.array(valid_tickets)
possible_range_map = dict()
for key in ranges_dict.keys():
    valid_idx = []
    for idx in range(len(ranges_dict)):
        if is_valid_field(ranges_dict[key], valid_ticket_mat[:,idx]):
            valid_idx.append(idx)
    # print(key, valid_idx)
    possible_range_map[key] = valid_idx


# Find a valid position for all field on the ticket
def find_smallest_list(nested_list):
    min_len = len(nested_list[0])
    min_idx = 0
    for i, l in enumerate(nested_list):
        if len(l) < min_len:
            min_len = len(l)
            min_idx = i
    return min_len, min_idx


range_map = dict()
while len(possible_range_map) > 0:
    min_len, idx = find_smallest_list(list(possible_range_map.values()))
    assert min_len == 1

    key = list(possible_range_map.keys())[idx]
    val = possible_range_map.pop(key)[0]
    range_map[key] = val

    # Remove the idx from all values
    for k in possible_range_map.keys():
        try:
            possible_range_map[k].remove(val)
        except ValueError:
            pass

# Find the six field on my ticket that start with the word departure
result = 1
for key in range_map.keys():
    if re.findall("^departure", key):
        # print(key)
        result *= int(my_ticket[range_map[key]])
print(result)

