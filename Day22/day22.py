import re
import math
import itertools
import numpy as np
from collections import defaultdict




if __name__ == "__main__":
    # # with open("input_small.txt") as infile:
    # with open("input.txt") as infile:
    #     raw = infile.read()

    # input_raw = [line for line in raw.split('\n') if line.strip()]


    player1 = [42,29,12,40,47,26,11,39,41,13,8,50,44,33,5,27,10,25,17,1,28,22,6,32,35]
    player2 = [19, 34, 38, 21, 43, 14, 23, 46, 16, 3, 36, 31, 37, 45, 30, 15, 49, 48, 24, 9, 2, 18, 4, 7, 20]

    while player1 and player2:
        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if p1 > p2:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)
    
    if player1:
        answer = 0
        for i, card in enumerate(player1):
            answer += (len(player1) - i) * card

    elif player2:
        answer = 0
        for i, card in enumerate(player2):
            answer += (len(player2) - i) * card

    print(answer)