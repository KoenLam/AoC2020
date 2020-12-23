import re

eq = "1 + (2 * 3) + (4 * (5 + 6))"

# t = re.findall("\(.*\)", eq)

def find_parenthesis(eq):
    match = []
    num_paren = 0
    inside_paren = False
    for l in eq:
        if l == "(":
            if num_paren == 0:
                match.append("")
            else:
                match[-1] += l

            num_paren += 1
            inside_paren = True
        elif l == ")":
            num_paren -= 1
            if num_paren == 0:
                inside_paren = False
            else:
                match[-1] += l
        elif inside_paren:
            match[-1] += l
    return match

print(find_parenthesis(eq))