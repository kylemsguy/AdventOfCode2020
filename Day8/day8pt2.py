
def execute(program):
    pc = 0
    acc = 0
    executed = []
    while pc not in executed:
        if pc >= len(program):
            print("Boot sequence done")
            break
        # print(pc, len(program))
        ins, arg = program[pc].split(' ')
        if ins == 'acc':
            acc += int(arg)
        elif ins == 'jmp':
            pc += int(arg) - 1
        elif ins == 'nop':
            pass
        else:
            print("Invalid instruction", ins)
            exit(1)
        executed.append(pc)
        pc += 1

    return pc, acc

if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    lines = [line.strip() for line in raw.split('\n') if line.strip()]

    for i, line in enumerate(lines):
        new_prog = lines[:]
        ins, arg = line.split(' ')
        if ins == 'nop':
            # try
            new_prog[i] = ' '.join(['jmp', arg])
        elif ins == 'jmp':
            new_prog[i] = ' '.join(['nop', arg])
        else:
            continue
        pc, acc = execute(new_prog)
        if pc > 659:
            print(i, line, acc)
            break
