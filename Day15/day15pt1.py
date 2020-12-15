import re
import copy
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
    ages_next = {
        13: 5,
        16: 4,
        0: 3,
        12: 2,
        15: 1,
        1: 0,
    }
    nums = [13,16,0,12,15,1]
    curr_idx = len(nums)

    last_added = None
    while len(nums) < 2020:
        num = nums[-1]
        if num not in ages:
            ages_next[num] = 0
            to_add = 0
        else:
            to_add = ages[num]
            ages_next[num] = 0
        nums.append(to_add)
        for n in ages_next:
            ages_next[n] += 1
        ages = copy.deepcopy(ages_next)
    
    print(nums[-1])
