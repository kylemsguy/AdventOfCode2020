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


def consecutive_bus(schedule):
    # This should be a list of tuples (a, n) such that x = a (mod n)
    s = [(-i, schedule[i]) for i in range(len(schedule)) if schedule[i]]
    r_i = [x[0] for x in s] # remainders
    m_i = [x[1] for x in s] # divisors
    M = functools.reduce(lambda x, y: x * y, m_i)
    
    m1 = m_i[0]
    m2 = m_i[1]
    n1 = r_i[0]
    n2 = r_i[1]

    a1, a2 = bezout_coeff(m1, m2)
    x = a1*m1*n2 + a2*m2*n1

    for i in range(2, len(s)):
        m1 = m1 * m2
        m2 = m_i[i]
        n1 = x
        n2 = r_i[i]
        a1, a2 = bezout_coeff(m1, m2)
        x = a1*m1*n2 + a2*m2*n1
    return x % M


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
    print(consecutive_bus(schedule))
