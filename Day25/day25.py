import os
import sys
import re
import math
import copy
import itertools
import numpy as np
from collections import defaultdict

def get_loopsize(pubkey):
    value = 1
    subject = 7
    i = 0
    while value != pubkey:
        value = value * subject
        value = value % 20201227
        i += 1
        # print(value)

    return i


def encrypt_subject(subject, iterations):
    value = 1
    for i in range(iterations):
        value = value * subject
        value = value % 20201227

    return value


if __name__ == "__main__":
    # # with open("input_small.txt") as infile:
    with open("input.txt") as infile:
        raw = infile.read()

    input_raw = [int(line) for line in raw.split('\n') if line.strip()]

    value = 1
    div = 20201227

    card_pubkey, door_pubkey = input_raw

    # Derive card's loop size
    
    # door_loopsize = get_loopsize(door_pubkey)
    # print(door_loopsize)
    card_loopsize = get_loopsize(card_pubkey)

    enckey = encrypt_subject(door_pubkey, card_loopsize)

    print(enckey)