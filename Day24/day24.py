import os
import sys
import re
import math
import copy
import itertools
import numpy as np
from collections import defaultdict


def get_min_max(tiles):
    coords = list(tiles.keys())
    min_row, min_col, max_row, max_col = 1e99, 1e99, -1e99, -1e99
    for row, col in coords:
        if row < min_row:
            min_row = row
        if row > max_row:
            max_row = row
        if col < min_col:
            min_col = col
        if col > max_col:
            max_col = col
    return min_row, min_col, max_row, max_col
    

def count_neighbours(tiles, row, col):
    ne = row - 1, col
    nw = row - 1, col - 1
    w = row, col - 1
    e = row, col + 1
    sw = row + 1, col
    se = row + 1, col + 1

    return tiles[ne] + tiles[nw] + tiles[w] + tiles[e] + tiles[sw] + tiles[se]


if __name__ == "__main__":
    # # with open("input_small.txt") as infile:
    with open("input.txt") as infile:
        raw = infile.read()

    input_raw = [line for line in raw.split('\n') if line.strip()]

    tile_refs = []

    for line in input_raw:
        tile = []
        i = 0
        while i < len(line):
            if line[i] in ['n', 's']:
                tile.append(line[i:i+2])
                i += 2
            else:
                tile.append(line[i])
                i += 1

        tile_refs.append(tile)

    tile_board = defaultdict(bool)

    for tile in tile_refs:
        r, c = 0, 0
        for ref in tile:
            if ref == 'ne':
                r -= 1
            elif ref == 'nw':
                r -= 1
                c -= 1
            elif ref == 'w':
                c -= 1
            elif ref == 'e':
                c += 1
            elif ref == 'sw':
                r += 1
            elif ref == 'se':
                r += 1
                c += 1

        curr = tile_board[(r, c)]
        
        tile_board[(r, c)] = not curr

    b_up = 0
    for c in tile_board:
        b_up += tile_board[c]

    for ref in tile_refs:
        print(ref)
    print(b_up)

    min_row, min_col, max_row, max_col = get_min_max(tile_board)

    # Part 2
    for i in range(100):
        min_row -= 1
        min_col -= 1
        max_row += 1
        max_col += 1
        new_board = copy.deepcopy(tile_board)
        for row in range(min_row, max_row+1):
            for col in range(min_col, max_col+1):
                n = count_neighbours(tile_board, row, col)
                if tile_board[(row, col)]:
                    if n == 0 or n > 2:
                        new_board[(row, col)] = False
                else:
                    if n == 2:
                        new_board[(row, col)] = True

        tile_board = new_board


    b_up = 0
    for c in tile_board:
        b_up += tile_board[c]

    print(b_up)
