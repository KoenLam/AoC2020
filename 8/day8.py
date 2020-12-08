


with open("input") as f:
    opcodes = f.read().strip().split("\n")


print("Puzzle 1")
acc = 0
pc = 0
pcs = []

while pc < len(opcodes):
    if pc not in pcs:
        pcs.append(pc)
    else:
        break
    opcode, instr = opcodes[pc].split()
    print(opcode, instr)
    if opcode == "acc":
        acc += eval(instr)
    elif opcode == "jmp":
        pc += eval(instr)
        continue
    pc += 1
print(acc)

print("Puzzle 2")

def run_machine(opcodes):
    finished = True
    acc = 0
    pc = 0
    pcs = []

    while pc < len(opcodes):
        if pc not in pcs:
            pcs.append(pc)
        else:
            finished = False
            break
        opcode, instr = opcodes[pc].split()
        # print(pc, opcode, instr)
        if opcode == "acc":
            acc += eval(instr)
        elif opcode == "jmp":
            pc += eval(instr)
            continue
        pc += 1
    return finished, acc


opcodes_copy = opcodes.copy()

# Find all jumps and nops
jumps = [pc for pc, instr in enumerate(opcodes) if instr.split()[0] == "jmp"]
nops = [pc for pc, instr in enumerate(opcodes) if instr.split()[0] == "nop"]

stop = False

for jump in jumps:
    opcodes = opcodes_copy.copy()

    opcodes[jump] = opcodes[jump].replace("jmp", "nop")
    print("CHANGED jmp to", opcodes[jump] )
    finish, acc = run_machine(opcodes)
    if finish:
        stop = True
        break

if not stop:
    for nop in nops:
        opcodes = opcodes_copy.copy()

        opcodes[nop] = opcodes[nop].replace("nop", "jmp")
        print("CHANGED nop to", opcodes[nop] )
        finish, acc = run_machine(opcodes)
        if finish:
            stop = True
            break
print(stop, acc)
