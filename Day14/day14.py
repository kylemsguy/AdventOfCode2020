import re
from collections import defaultdict


class Mask:
    def __init__(self, mask):
        self.mask = mask
        self.actual_masks = []
        # mask = 010X1100101X00X01001X11010X111100X01
        for i, bit in enumerate(mask):
            if bit == '0':
                op = '+'
                mask = ~(1 << (35 - i))
            elif bit == '1':
                op = '|'
                mask = 1 << (35 - i)
            else:
                continue
            self.actual_masks.append((op, mask))

    def apply(self, value):
        for op, mask in self.actual_masks:
            if op == '+':
                value = value & mask
            elif op == '|':
                value = value | mask
        return value


if __name__ == "__main__":
    with open("input.txt") as infile:
    # with open("input_short.txt") as infile:
        raw = infile.readlines()

    mem = defaultdict(int)

    curr_mask = None
    for line in raw:
        line = line.strip()
        m_mask = re.match("mask = (.*)", line)
        if m_mask:
            mask = m_mask.group(1)
            curr_mask = Mask(mask)
        elif m_write := re.match("mem\[(.*?)\] = (.*)", line):
            # print(line)
            addr = int(m_write.group(1))
            value = int(m_write.group(2))
            masked_val = curr_mask.apply(value)
            mem[addr] = masked_val
        else:
            print("ERROR")
            print(line)
            exit(1)

    sol = sum(list(mem.values()))
    print(sol)
