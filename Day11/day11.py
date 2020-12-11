import copy

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
            

def seats_next(seats):
    new_seats = copy.deepcopy(seats)
    for r in range(len(seats)):
        for c in range(len(seats[0])):
            if seats[r][c] == 'L':
                if count_adjacent_occupied(seats, r, c) == 0:
                    new_seats[r][c] = '#'
            elif seats[r][c] == '#':
                if count_adjacent_occupied(seats, r, c) >= 4:
                    new_seats[r][c] = 'L'
    return new_seats


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


if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    seats = [list(line) for line in raw.split('\n') if line.strip()]
    
    prev_seats = seats
    next_seats = seats_next(seats)
    while not seats_equal(prev_seats, next_seats):
        prev_seats = next_seats
        next_seats = seats_next(prev_seats)
    count = count_occupied(next_seats)
    print(count)
