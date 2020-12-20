import re
import math
import itertools
import numpy as np
from collections import defaultdict


class Tile:
    def __init__(self, tile_id):
        self.tile_id = tile_id
        self.raw_data = []
        self.data = None
        self.transformations = []

    def __repr__(self):
        return f"Tile {self.tile_id}"

    def rotate(self):
        self.transformations.append("rotateleft")
        # only rotates left
        self.data = np.rot90(self.data)#, times)

    def undo_transformation(self):
        pass

    def flip(self, axis):
        if axis == 'x':
            self.transformations.append('flip_x')
            self.data = np.fliplr(self.data)
            return True
        elif axis == 'y':
            self.transformations.append('flip_y')
            self.data = np.flipud(self.data)
            return True
        else:
            print(axis)
            return False

    def get_edges(self):
        top_row = self.data[0, :]
        bottom_row = self.data[-1, :]
        left_row = self.data[:, 0]
        right_row = self.data[:, -1]
        return top_row, bottom_row, left_row, right_row

    def edge_matches(self, other, direction):
        m_edges = self.get_edges()
        o_edges = other.get_edges()

        if direction == 'up':
            return (m_edges[0] == o_edges[1]).all()
        elif direction == 'down':
            return (m_edges[1] == o_edges[0]).all()
        elif direction == 'left':
            return (m_edges[2] == o_edges[3]).all()
        elif direction == 'left':
            return (m_edges[3] == o_edges[2]).all()

        raise ValueError(direction1)


def get_empty_tile(array):
    for row in range(array.shape[0]):
        for col in range(array.shape[1]):
            if array[row, col] == 0:
                return row, col
    return None


def check_neighbours(array, rowcol):
    row, col = rowcol
    tile = array[row, col]

    # up
    if row - 1 >= 0:
        other = array[row-1, col]
        if other and not tile.edge_matches(other, 'up'):
            return False
    # down
    if row + 1 < array.shape[0]:
        other = array[row+1, col]
        if other and not tile.edge_matches(other, 'down'):
            return False
    # left
    if col - 1 >= 0:
        other = array[row, col-1]
        if other and not tile.edge_matches(other, 'left'):
            return False
    # right
    if col + 1 < array.shape[1]:
        other = array[row, col+1]
        if other and not tile.edge_matches(other, 'right'):
            return False

    return True


def find_solution(unplaced_tiles, array):
    rowcol = get_empty_tile(array)
    if not rowcol:
        return True
    row, col = get_empty_tile(array)
    for tile in unplaced_tiles:
        array[row, col] = tile
        # No flips
        for i in range(4):
            is_valid = check_neighbours(array, (row, col))
            if is_valid:
                if find_solution(unplaced_tiles - {tile}, array):
                    return True
            tile.rotate()
        # Flip x
        tile.flip('x')
        for i in range(4):
            is_valid = check_neighbours(array, (row, col))
            if is_valid:
                if find_solution(unplaced_tiles - {tile}, array):
                    return True
            tile.rotate()
        # Flip x&y
        tile.flip('y')
        for i in range(4):
            is_valid = check_neighbours(array, (row, col))
            if is_valid:
                if find_solution(unplaced_tiles - {tile}, array):
                    return True
            tile.rotate()
        # Flip y
        tile.flip('x')
        for i in range(4):
            is_valid = check_neighbours(array, (row, col))
            if is_valid:
                if find_solution(unplaced_tiles - {tile}, array):
                    return True
            tile.rotate()
        tile.flip('y')

        array[row, col] = 0

    return (array != 0).all()


if __name__ == "__main__":
    # with open("input_small.txt") as infile:
    with open("input.txt") as infile:
        raw = infile.read()

    input_raw = [line for line in raw.split('\n') if line.strip()]

    tiles = []
    current_tile = None
    for line in input_raw:
        if line.startswith("Tile"):
            if current_tile:
                tiles.append(current_tile)
                current_tile = None
            id_match = re.match(r"Tile (\d+):", line)
            tile_id = int(id_match.group(1))
            current_tile = Tile(tile_id)
        else:
            current_tile.raw_data.append(list(line))

    if current_tile:
        tiles.append(current_tile)

    for tile in tiles:
        tile.data = np.array(tile.raw_data)

    print(len(tiles))

    dim = int(math.sqrt(len(tiles)))

    unplaced_tiles = set(tiles)
    array = np.zeros(shape=(dim, dim), dtype=object)
    solution = find_solution(unplaced_tiles, array)

    print(solution)

    result = (array[0,0].tile_id * 
                array[0,-1].tile_id * 
                array[-1,0].tile_id *
                array[-1,-1].tile_id)

    print(result)

    
    # do fancy rotations to try to match stuff

