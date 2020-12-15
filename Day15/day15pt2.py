import re
import copy
import time
from collections import defaultdict


if __name__ == "__main__":
    ages = {
        13: 5,
        16: 4,
        0: 3,
        12: 2,
        15: 1,
        # 1: 0,
    }
    ages = {
        13: 0,
        16: 1,
        0: 2,
        12: 3,
        15: 4,
        # 1: 0,
    }
    nums = [13,16,0,12,15,1]
    curr_idx = len(nums)

    last_added = None
    i = 0
    t = time.time()
    while len(nums) < 30000000:
    # while len(nums) < 2020:
        i += 1
        if i % 1000000 == 0:
            curr = time.time()
            print(i)
            print(curr - t)
            t = curr
        # updates = {}
        num = nums[-1]
        if num not in ages:
            to_add = 0
            updates[num] = len(nums) - 1
        else:
            to_add = len(nums) - ages[num] - 1
            updates[num] = len(nums) - 1
        nums.append(to_add)
        for key, val in updates.items():
            ages[key] = val
    
    print(nums[-1])
