import re
import math
import itertools
import numpy as np
from collections import defaultdict

class Cup:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return "Cup " + str(self.val)

num_cup_map = {}


def pick_up(current):
    first = current.next
    last = first.next.next

    current.next = last.next
    last.next.prev = first

    first.prev = None
    last.next = None

    contents = []
    curr = first
    while curr != None:
        contents.append(curr.val)
        curr = curr.next

    return first, contents


def insert_after(dest, lst):
    d = num_cup_map[dest]
    last = lst.next.next

    lst.prev = d
    last.next = d.next
    d.next.prev = last
    d.next = lst


if __name__ == "__main__":
    # # with open("input_small.txt") as infile:
    # with open("input.txt") as infile:
    #     raw = infile.read()

    # input_raw = [line for line in raw.split('\n') if line.strip()]

    start = "962713854"
    # start = "389125467"

    num = int(start[0])
    first_obj = Cup(num)
    num_cup_map[num] = first_obj
    prev_obj = first_obj
    for n in start[1:]:
        num = int(n)
        num_obj = Cup(num)
        num_obj.prev = prev_obj
        prev_obj.next = num_obj
        num_cup_map[num] = num_obj
        prev_obj = num_obj

    for num in range(10, 1000001):
        num_obj = Cup(num)
        num_obj.prev = prev_obj
        prev_obj.next = num_obj
        num_cup_map[num] = num_obj
        prev_obj = num_obj

    prev_obj.next = first_obj
    first_obj.prev = prev_obj

    print("Sanity Check: # Cups", len(num_cup_map))

    max_cup = 1000000
    min_cup = 1
    num_cups = 1000000

    curr_cup = first_obj
    for i in range(10000000):
        if (i+1) % 1000000 == 0:
            print("Iteration", i+1)
        lst, picked_up = pick_up(curr_cup)
        # select destination
        dst = curr_cup.val - 1
        if dst < min_cup:
            dst = max_cup
        while dst in picked_up:
            dst -= 1
            if dst < min_cup:
                dst = max_cup

        insert_after(dst, lst)

        curr_cup = curr_cup.next


    cup_1 = num_cup_map[1]

    answer = cup_1.next.val * cup_1.next.next.val

    print("Part 2 Solution:", answer)
