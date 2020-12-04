with open("input.txt") as infile:
    input_data = infile.readlines()

input_map = [line.strip("\n") for line in input_data]

row, col = 0, 0
width = len(input_map[0])

tree_count = 0
while row < len(input_map):
    if input_map[row][col] == '#':
        print(f"({row}, {col}): Ouch!")
        tree_count += 1
    row += 1
    col = (col + 3) % width

print("Trees encountered:", tree_count)