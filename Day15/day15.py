import re
import copy
import time
from collections import defaultdict

def memory_game(nums, limit, last_encountered=None, print_interval=0):
    """Generates the list of numbers after <limit> iterations of Day 14's 
        number game

    Args:
        nums (list(int)): Initial list of numbers
        limit (int): Maximum number of iterations
        last_encountered (dict(int:int), optional): A cached last_encountered
            list from a previous run, if any. Defaults to None.
        print_interval (int, optional): The number of iterations to print 
            runtime at. If 0, this is disabled. Defaults to 0.

    Returns:
        [type]: [description]
    """
    if not last_encountered:
        last_encountered = {num: i for i, num in enumerate(nums[:-1])}

    i = 0
    t = time.time()
    while len(nums) < limit:
        num = nums[-1]
        if num not in last_encountered:
            to_add = 0
        else:
            to_add = len(nums) - last_encountered[num] - 1
        last_encountered[num] = len(nums) - 1
        nums.append(to_add) 
        i += 1
        if print_interval > 0 and i % print_interval == 0:
            curr = time.time()
            print(f"Iteration {i-print_interval+1}-{i}: {curr - t} sec")
            t = curr   
    if print_interval > 0:
        curr = time.time()
        print(f"Iteration {i - (i % print_interval) + 1}-{i}: {curr - t} sec")

    return last_encountered

if __name__ == "__main__":
    nums = [13,16,0,12,15,1]
    print("Initial nums:", nums)
    p1_la = memory_game(nums, 2020)
    print("Part 1 answer:", nums[-1])
    start_time = time.time()
    p2_la = memory_game(nums, 30000000, last_encountered=p1_la, print_interval=10000000)
    print(f"Part 2 answer: {nums[-1]} (time elapsed: {time.time() - start_time} sec)")
