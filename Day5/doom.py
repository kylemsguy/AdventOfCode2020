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
    max_id = -1
    for line in lines:
        row, col = get_row_col(line)
        seat_id = get_seat_id(row, col)
        if seat_id > max_id:
            max_id = seat_id

    print("Max ID:", max_id)
