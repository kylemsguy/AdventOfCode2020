import re
import math
import itertools
import numpy as np
from collections import defaultdict


# def pop_next_three

if __name__ == "__main__":
    # # with open("input_small.txt") as infile:
    # with open("input.txt") as infile:
    #     raw = infile.read()

    # input_raw = [line for line in raw.split('\n') if line.strip()]

    start = "962713854"
    # start = "389125467"

    cups = [int(x) for x in start]

    max_cup = max(cups)
    min_cup = min(cups)
    num_cups = len(cups)

    curr_idx = 0
    for i in range(100):
        print("cups", cups)
        curr = cups[curr_idx]
        print("curr", curr)
        picked_up = []
        for i in range(3):
            next_cup = (curr_idx + i + 1) % num_cups
            # print(next_cup)
            picked_up.append(cups[next_cup])
        for c in picked_up:
            cups.remove(c)

        print("Pick up", picked_up)

        dest = curr - 1
        if dest < min_cup:
            dest = max_cup
        while dest in picked_up:
            dest = dest - 1
            if dest < min_cup:
                dest = max_cup
        print("dest", dest)
        index = cups.index(dest)
        for cup in picked_up[::-1]:
            cups.insert(index+1, cup)
        curr_idx = (cups.index(curr) + 1) % num_cups

    cup_1_i = cups.index(1)
    print(cups)
    for i in range(num_cups-1):
        index = (cup_1_i + i + 1) % num_cups
        print(cups[index], end='')

    print()
