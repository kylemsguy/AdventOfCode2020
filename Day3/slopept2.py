import math

def count_trees(tree_map, right, down):
    row, col = 0, 0
    width = len(tree_map[0])

    tree_count = 0
    while row < len(tree_map):
        if tree_map[row][col] == '#':
            # print(f"({row}, {col}): Ouch!")
            tree_count += 1
        row += down
        col = (col + right) % width

    print(f"Trees encountered for ({right} right, {down} down):", tree_count)
    return tree_count

if __name__ == "__main__":
    with open("input.txt") as infile:
        input_data = infile.readlines()
        
    input_map = [line.strip("\n") for line in input_data]

    paths = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    # for right, down in paths:
    #     tree_count = count_trees(input, right, down)

    result = math.prod([count_trees(input_map, right, down) for right, down in paths])

    print("Product of all trees on all paths:", result)