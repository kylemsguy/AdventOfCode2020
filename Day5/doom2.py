with open("input.txt") as infile:
    raw = infile.read()

lines = [line.strip() for line in raw.split('\n')]

def get_row_col(bsp):
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7

    for l in bsp:
        if l == 'F':
            max_row = (max_row - min_row + 1) / 2 - 1 + min_row
        elif l == 'B':
            min_row = (max_row - min_row + 1) / 2 + min_row
        elif l == 'L':
            max_col = (max_col - min_col + 1) / 2 - 1 + min_col
        elif l == 'R':
            min_col = (max_col - min_col + 1) / 2 + min_col
        # print(min_row, max_row, min_col, max_col)
        
    return min_row, min_col


def get_seat_id(row, col):
    return row * 8 + col

if __name__ == "__main__":
    seat_list = []
    min_row = 99999
    max_row = -1
    for line in lines:
        row, col = get_row_col(line)
        if row < min_row:
            min_row = row
        if row > max_row:
            max_row = row
        seat_id = get_seat_id(row, col)
        seat_list.append(seat_id)

    print('asdf', min_row, max_row)

    seat_list.sort()
    # print(seat_list)
    for i in range(len(seat_list) - 1):
        if seat_list[i+1] != seat_list[i] + 1:
            print(seat_list[i], seat_list[i+1])

    # print(max_id)
