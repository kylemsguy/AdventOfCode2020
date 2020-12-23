import sys


def init_part2(nums):
    cups = [0 for _ in range(1000001)]
    cups[0] = None

    prev = nums[0]
    for i in nums[1:]:
        cups[prev] = i
        prev = i

    for i in range(10, 1000001):
        cups[prev] = i
        prev = i

    cups[-1] = nums[0]
    return cups


def pick_up(cups, curr):
    start = cups[curr]
    middle = cups[start]
    end = cups[middle]

    cups[curr] = cups[end]
    cups[end] = 0

    picked_up = [start, middle, end]

    return picked_up
    

def insert_after(cups, picked_up, dest):
    end = picked_up[-1]
    cups[end] = cups[dest]
    cups[dest] = picked_up[0]


def select_dest(cups, picked_up, curr):
    dest = curr - 1
    if dest < 1:
        dest = len(cups) - 1
    while dest in picked_up:
        dest -= 1
        if dest < 1:
            dest = len(cups) - 1
    return dest
    

if __name__ == "__main__":
    # # with open("input_small.txt") as infile:
    # with open("input.txt") as infile:
    #     raw = infile.read()

    # input_raw = [line for line in raw.split('\n') if line.strip()]

    start = "962713854"
    # start = "389125467"

    nums = [int(x) for x in start]

    cups = [None] + nums

    curr_cup = nums[0]
    for i in range(100):
        picked_up = pick_up(cups, curr_cup)
        # select destination
        dest = select_dest(cups, picked_up, curr_cup)
        # print(dest)

        insert_after(cups, picked_up, dest)

        curr_cup = cups[curr_cup]

    print("Part 1 solution: ", end='')
    i = cups[1]
    while i != 1:
        print(i, end='')
        i = cups[i]
    print()

    print("Part 2 solution: ", end='')
    sys.stdout.flush()

    cups = init_part2(nums)

    curr_cup = nums[0]
    for i in range(10000000):
        # if (i+1) % 1000000 == 0:
        #     print("Iteration", i+1)
        picked_up = pick_up(cups, curr_cup)
        # select destination
        dest = select_dest(cups, picked_up, curr_cup)
        # print(dest)

        insert_after(cups, picked_up, dest)

        curr_cup = cups[curr_cup]



    answer = cups[1] * cups[cups[1]]

    print(answer)
