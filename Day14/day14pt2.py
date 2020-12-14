import re
from collections import defaultdict
from itertools import combinations


class Mask:
    # V2
    def __init__(self, mask):
        self.mask = mask
        self.set_mask = 0
        self.floating = []
        # mask = 010X1100101X00X01001X11010X111100X01
        for i, bit in enumerate(mask):
            if bit == '0':
                continue
            elif bit == '1':
                mask = 1 << (35 - i)
                self.set_mask |= mask
            else: # bit == 'X'
                # handle floating
                # self.floating.append(1 << (35 - i))
                self.floating.append(i)

    def apply(self, value):
        values = []
        value |= self.set_mask
        for i in range(len(self.floating)):
            num = i + 1
            masks = combinations(self.floating, num)

            for m in masks:
                complement_masks = [x for x in self.floating if x not in m]
                c_mask = 0
                for idx in complement_masks:
                    c_mask |= 1 << (35 - idx)
                c_mask = ~c_mask
                mask_set = value & c_mask
                mask_unset = value & c_mask

                actual_mask = 0
                for idx in m:
                    actual_mask |= 1 << (35 - idx)
                mask_set |= actual_mask
                mask_unset &= ~actual_mask
                values.append(mask_set)
                values.append(mask_unset)
        return values
            


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
            actual_addrs = curr_mask.apply(addr)
            for a in actual_addrs:
                mem[a] = value
        else:
            print("ERROR")
            print(line)
            exit(1)

    sol = sum(list(mem.values()))
    print(sol)
