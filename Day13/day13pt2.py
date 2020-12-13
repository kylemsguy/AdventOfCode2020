import sys
import math


import functools

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

def bezout_coeff(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return old_s, old_t


def consecutive_bus4(schedule):
    # This should be a list of tuples (a, n) such that x = a (mod n)
    s = [(i, schedule[i]) for i in range(len(schedule)) if schedule[i]]
    r_i = [x[0] for x in s]
    m_i = [x[1] for x in s]
    M = functools.reduce(lambda x, y: x * y, m_i)
    a_i = [M // m for m in m_i]
    i_i = [a % m for a, m in zip(a_i, m_i)]

    Z = sum([i * r * a for i, r, a in zip(i_i, r_i, a_i)])

    return Z % M

def consecutive_bus5(schedule):
    # This should be a list of tuples (a, n) such that x = a (mod n)
    s = [(i, schedule[i]) for i in range(len(schedule)) if schedule[i]]
    r_i = [x[0] for x in s] # remainders
    m_i = [x[1] for x in s] # divisors

    m1, m2 = m_i[:2]
    r1, r2 = r_i[:2]

    a, b = bezout_coeff(m1, m2)
    result = a * m1 * r2 + b * m2 * r1 + (m1 * m2)

    for i in range(2, len(s)):
        m1 = m1 * m_i[i-1]
        m2 = m_i[i]

        r1 = result
        r2 = r_i[i]

        result = a * m1 * r2 + b * m2 * r1 + (m1 * m2)
    
    return result


def consecutive_bus6(schedule):
    # This should be a list of tuples (a, n) such that x = a (mod n)
    s = [(i, schedule[i]) for i in range(len(schedule)) if schedule[i]]
    r_i = [x[0] for x in s] # remainders
    m_i = [x[1] for x in s] # divisors
    M = functools.reduce(lambda x, y: x * y, m_i)
    a_i = [M // m for m in m_i]
    Z = sum([bezout_coeff(a_i[i], m_i[i])[0] * a_i[i] * a_i[i] for i in range(len(s))])

    return Z % M


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
    print(consecutive_bus4(schedule))
    print(consecutive_bus5(schedule))
    print(consecutive_bus6(schedule))
