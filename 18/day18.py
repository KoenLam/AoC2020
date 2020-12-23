import re

with open("input") as f:
    eqs = [l.replace(" ", "") for l in f.read().strip().split("\n")]


print("Puzzle 1")
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


def eval_equation(eq):
    sub_parentheses = find_parenthesis(eq)
    for parentheses in sub_parentheses:
        repl = str(eval_equation(parentheses))
        eq = eq.replace(f"({parentheses})", repl)

    if find_parenthesis(eq):
        return eval_equation(eq)

    # print("HERE", eq)
    add = lambda a, b: a + b
    mul = lambda a, b: a * b
    
    result = 0
    op = add

    eq = eq.replace("+", " + ").replace("*", " * ").split()
    for l in eq:
        if re.match("\d", l):
            result = op(result, int(l))
        elif re.match("\+", l):
            op = add
        elif re.match("\*", l):
            op = mul
    # print("RESULT", result)
    return result

result = 0
for eq in eqs:
    result += eval_equation(eq)
print(result)


print("Puzzle 2")

def find_after_plus(eq):
    match = ""
    num_parent = 0
    for l in eq:
        if l == "(":
            num_parent += 1
        elif l == ")":
            num_parent -= 1
            if num_parent == 0:
                match += l
                break
            elif num_parent < 0:
                break
        elif (l == "+" or l == "*") and num_parent == 0:
            break
        match += l
    return match


def find_before_plus(eq):
    match = ""
    match = ""
    num_parent = 0
    for l in eq[::-1]:
        if l == ")":
            num_parent += 1
        elif l == "(":
            num_parent -= 1
            if num_parent == 0:
                match += l
                break
            elif num_parent < 0:
                break
        elif (l == "+" or l == "*") and num_parent == 0:
            break
        match += l
    return match[::-1]


def plus_add_parenthesis(eq):
    i = 0
    while i < len(eq):
        l = eq[i]

        if l == "+":
            after = find_after_plus(eq[i+1:])
            before = find_before_plus(eq[:i])
            eq = eq[:i-len(before)] \
                + f"({before}+{after})" \
                + eq[i+len(after)+1:] 
            i +=  1 # To compensate for the extra parenthesis

        i += 1
    return eq


result = 0
for eq in eqs:
    eq = plus_add_parenthesis(eq)
    result += eval_equation(eq)
print(result)