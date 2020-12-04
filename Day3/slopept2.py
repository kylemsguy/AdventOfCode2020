import sys

with open("input.txt") as infile:
    input_data = infile.readlines()

input_map = [line.strip("\n") for line in input_data]

def count_trees(tree_map, right, down):
    row, col = 0, 0
    width = len(tree_map[0])

    tree_count = 0
    while row < len(tree_map):
        if tree_map[row][col] == '#':
            print(f"({row}, {col}): Ouch!")
            tree_count += 1
        row += down
        col = (col + right) % width

    print("Trees encountered:", tree_count)