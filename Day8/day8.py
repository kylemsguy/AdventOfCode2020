if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    lines = [line.strip() for line in raw.split('\n') if line.strip()]

    pc = 0
    acc = 0
    executed = []
    while pc not in executed:
        ins, arg = lines[pc].split(' ')
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

    print(acc)
