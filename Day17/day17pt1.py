import copy


def count_neighbours(state, x, y, z):
    num_neighbours = 0
    for i in range(-1, 2):
        curr_x = x + i
        if curr_x < 0 or curr_x >= len(state[0][0]):
            continue
        for j in range(-1, 2):
            curr_y = y + j
            if curr_y < 0 or curr_y >= len(state[0]):
                continue
            for k in range(-1, 2):
                curr_z = z + k
                if curr_z < 0 or curr_z >= len(state):
                    continue
                if curr_x == x and curr_y == y and curr_z == z:
                    continue

                # print(curr_z,curr_y,curr_x)

                num_neighbours += state[curr_z][curr_y][curr_x]

    return num_neighbours


def expand_state(state):
    old_x, old_y, old_z = (len(state[0][0]), len(state[0]), len(state))
    new_dimensions = old_x + 2, old_y + 2, old_z + 2
    for z in range(old_z):
        for y in range(old_y):
            state[z][y].insert(0, False)
            state[z][y].append(False)

    for z in range(old_z):
        state[z].insert(0, [False for _ in range(new_dimensions[1])])
        state[z].append([False for _ in range(new_dimensions[1])])
            
    state.insert(0, [[False for _ in range(new_dimensions[0])] for i in range(new_dimensions[1])])
    state.append([[False for _ in range(new_dimensions[0])] for i in range(new_dimensions[1])])


def next_state(state):
    expand_state(state)
    # pad the state with two new arrays
    new_state = copy.deepcopy(state)

    dim = len(state[0][0]), len(state[0]), len(state)

    for x in range(dim[0]):
        for y in range(dim[1]):
            for z in range(dim[2]):
                count = count_neighbours(state, x, y, z)
                if state[z][y][x]:
                    new_state[z][y][x] = (count == 2 or count == 3)
                else:
                    new_state[z][y][x] = (count == 3)

    return new_state

def print_layer(state, layer):
    l = state[layer]
    for row in l:
        print(['#' if c else '.' for c in row])


def count_cubes(state):
    count = 0
    for row in state:
        for col in row:
            for it in col:
                count += it

    return count

if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    state = [[[c == '#' for c in line] for line in raw.split('\n') if line.strip()]]
    # print(state)

    # print(count_neighbours(state, 0, 0, 0))
    # print(count_neighbours(state, 1, 0, 0))

    for i in range(6):
        state = next_state(state)
        # print(count_cubes(state))
        # print_layer(state, 1)

    print(count_cubes(state))