import copy


# Part 1 adjacent counting function
def count_adjacent_occupied(seats, row, col):
    rows = [row - 1, row, row + 1]
    cols = [col - 1, col, col + 1]

    rows = [r for r in rows if r >= 0 and r < len(seats)]
    cols = [c for c in cols if c >= 0 and c < len(seats[0])]
    count = 0
    for r in rows:
        for c in cols:
            if r == row and c == col:
                continue
            if seats[r][c] == '#':
                count += 1

    return count


# Part 2 adjacent counting function
def count_first_seen_occupied(seats, row, col):
    directions = ['N','E','S','W','NE','NW','SE','SW']
    
    count = 0
    for d in directions:
        if get_first_seen(seats, row, col, d):
            count += 1

    return count


# Helper to find whether the first seen seat is full
def get_first_seen(seats, row, col, direction):
    diff_r = 0
    diff_c = 0
    if 'N' in direction:
        diff_r = -1
    if 'S' in direction:
        diff_r = 1
    if 'W' in direction:
        diff_c = -1
    if 'E' in direction:
        diff_c = 1

    row += diff_r
    col += diff_c
    while row >= 0 and row < len(seats) and col >= 0 and col < len(seats[0]):
        if seats[row][col] == '#':
            return True
        elif seats[row][col] == 'L':
            return False
        else:
            row += diff_r
            col += diff_c
    return False
            

# General function for updating the state of seats
def seats_next(seats, count_adjacent_fn, threshold_leave):
    new_seats = copy.deepcopy(seats)
    for r in range(len(seats)):
        for c in range(len(seats[0])):
            if seats[r][c] == 'L':
                if count_adjacent_fn(seats, r, c) == 0:
                    new_seats[r][c] = '#'
            elif seats[r][c] == '#':
                if count_adjacent_fn(seats, r, c) >= threshold_leave:
                    new_seats[r][c] = 'L'
    return new_seats


# Helpers for running the simulation
def count_occupied(seats):
    count = 0
    for r in seats:
        for c in r:
            if c == '#':
                count += 1
    return count


def seats_equal(seats1, seats2):
    for r in range(len(seats1)):
        for c in range(len(seats2)):
            if seats1[r][c] != seats2[r][c]:
                return False
    return True


def run_to_completion(seats, count_adjacent_fn, threshold_leave):
    """Returns number of occupied seats"""
    prev_seats = seats
    next_seats = seats_next(seats, count_adjacent_fn, threshold_leave)
    while not seats_equal(prev_seats, next_seats):
        prev_seats = next_seats
        next_seats = seats_next(prev_seats, count_adjacent_fn, threshold_leave)
    count = count_occupied(next_seats)
    return count


if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    seats = [list(line) for line in raw.split('\n') if line.strip()]
    
    part1 = run_to_completion(seats, count_adjacent_occupied, 4)
    print("[Part 1] # occupied:", part1)

    part2 = run_to_completion(seats, count_first_seen_occupied, 5)
    print("[Part 2] # occupied:", part2)
