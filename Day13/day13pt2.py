import sys
import math


from functools import reduce

def lcm(denominators):
    return reduce(lambda a,b: a*b // math.gcd(a,b), denominators)

def earliest_bus(arrival, schedule):
    min_bus = None
    min_wait_time = 1e99
    for bus in schedule:
        wait_time = bus - (arrival % bus)
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            min_bus = bus
    return min_bus, min_wait_time

def consecutive_bus(schedule):
    start_mul = 0
    found_time = None
    upper_bound = lcm([s for s in schedule if s])
    while (start_t := start_mul * schedule[0]) < upper_bound:
        found = True
        for i in range(len(schedule)):
            if schedule[i]:
                curr_t = start_t + i
                if curr_t % schedule[i] != 0:
                    found = False
                    break
        if found:
            found_time = start_t
            break
        start_mul += 1
    return found_time

def consecutive_bus2(schedule):
    max_value = max([x for x in schedule if x])
    max_index = schedule.index(max_value)
    upper_bound = lcm([x for x in schedule if x])
    print("Max number of iterations:", upper_bound / max_value)
    found_time = None

    multiplier = 0
    while (max_t := multiplier * max_value) < upper_bound:
        found = True
        for i in range(len(schedule)):
            curr_t = max_t - (max_index - i)
            if schedule[i] is not None:
                if curr_t % schedule[i] != 0:
                    found = False
                    break

        if found:
            found_time = max_t - max_index
            break
        multiplier += 1

    return found_time

def consecutive_bus3(schedule):
    max_value = max([x for x in schedule if x])
    max_index = schedule.index(max_value)
    upper_bound = lcm([x for x in schedule if x])
    print("Max number of iterations:", upper_bound / max_value)
    found_time = None

    schedule_modded = [(i, schedule[i]) for i in range(len(schedule)) if schedule[i]]

    multiplier = 0
    while (max_t := multiplier * max_value) < upper_bound:
        # print(upper_bound - max_t)
        found = True
        for i, value in schedule_modded:
            curr_t = max_t - (max_index - i)
            q, r = divmod(curr_t, value)
            if r != 0:
                found = False
                break
 
        if found:
            found_time = max_t - max_index
            break
        multiplier += 1

    return found_time


def consecutive_bus4(schedule):
    pass


if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("Using default filename")
        filename = "input.txt"
    with open(filename) as infile:
        raw = infile.readlines()

    estimate = int(raw[0].strip())
    schedule = [int(x) if x != 'x' else None for x in raw[1].strip().split(',')]

    # b, w = earliest_bus(estimate, schedule)
    # print(b, w)
    # print(b * w)

    # Part 2
    print(consecutive_bus3(schedule))
