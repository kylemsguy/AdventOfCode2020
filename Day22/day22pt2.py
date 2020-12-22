import re
import math
import itertools
import numpy as np
from collections import defaultdict


def calc_score(deck):
    answer = 0
    for i, card in enumerate(deck):
        answer += (len(deck) - i) * card
    return answer


starting_state_winners_map = {}


def recursive_combat(player1, player2, game_num=1):
    # print("Starting Game on stackframe", game_num)
    # print("Player1:", player1)
    # print("Player2:", player2)
    initial_state = (tuple(player1), tuple(player2))
    if initial_state in starting_state_winners_map:
        # print("Repeat game with state")
        # print("Player1:", player1)
        # print("Player2:", player2)
        winner = starting_state_winners_map[initial_state]
        # print(f"The winner in frame {game_num} is Player {winner}!")
        return winner
    prev_states = []
    winner = 1
    while player1 and player2:
        if (state := (tuple(player1), tuple(player2))) in prev_states:
            break

        prev_states.append(state)

        p1 = player1.pop(0)
        p2 = player2.pop(0)

        # print("Next round start")
        # print("Player1:", player1, p1)
        # print("Player2:", player2, p2)

        w = None
        if len(player1) >= p1 and len(player2) >= p2:
            new_deck1 = player1[:p1][:]
            new_deck2 = player2[:p2][:]
            w = recursive_combat(new_deck1, new_deck2, game_num+1)
            # print("Back to ", game_num)
        else:
            w = 1 if p1 > p2 else 2
        if w == 1:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)

    if len(player1) == 0:
        winner = 2
    elif len(player2) == 0:
        winner = 1
    else:
        winner = 1
        # print("Player 1 wins by default")

    starting_state_winners_map[initial_state] = winner
    # print(f"The winner in frame {game_num} is Player {winner}!")

    return winner
    


if __name__ == "__main__":
    # # with open("input_small.txt") as infile:
    # with open("input.txt") as infile:
    #     raw = infile.read()

    # input_raw = [line for line in raw.split('\n') if line.strip()]

    player1 = [42,29,12,40,47,26,11,39,41,13,8,50,44,33,5,27,10,25,17,1,28,22,6,32,35]
    player2 = [19, 34, 38, 21, 43, 14, 23, 46, 16, 3, 36, 31, 37, 45, 30, 15, 49, 48, 24, 9, 2, 18, 4, 7, 20]

    # player1 = [9, 2, 6, 3, 1]
    # player2 = [5, 8, 4, 7, 10]

    w = recursive_combat(player1, player2)

    if w == 1:
        answer = calc_score(player1)

    else:
        answer = calc_score(player2)

    print(answer)