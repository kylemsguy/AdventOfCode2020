import re
import math
import itertools
import numpy as np
from collections import defaultdict

class Food:
    def __init__(self, ingredients, allergens):
        self.ing = set(ingredients)
        self.allerg = set(allergens)

    def __repr__(self):
        ingr = ' '.join(self.ing)
        allerg = ', '.join(self.allerg)
        return f"{ingr} ({allerg})"


if __name__ == "__main__":
    # with open("input_small.txt") as infile:
    with open("input.txt") as infile:
        raw = infile.read()

    input_raw = [line for line in raw.split('\n') if line.strip()]

    foods = []
    ingredients = set()
    allergens = set()

    allergen_probable_map = defaultdict(list)
    for line in input_raw:
        ingr_re = re.match(r"(.*?)\(contains (.*?)\)", line)
        ingrs = [x for x in ingr_re.group(1).split(' ') if x]
        allergs = [x for x in ingr_re.group(2).split(', ') if x]
        ingredients.update(ingrs)
        allergens.update(allergs)
        food = Food(ingrs, allergs)
        foods.append(food)

    could_allergens = set()
    for a in allergens:
        ingr_sets = []
        for f in foods:
            if a in f.allerg:
                ingr_sets.append(f.ing)
        if len(ingr_sets) > 1:
            could_allergens.update(ingr_sets[0].intersection(*ingr_sets[1:]))
        else:
            could_allergens.update(ingr_sets[0])


    not_allergens = ingredients - could_allergens
    print(not_allergens)

    ingr_occur_map = defaultdict(int)
    for f in foods:
        for ing in not_allergens:
            if ing in f.ing:
                ingr_occur_map[ing] += 1

    answer = sum(list(ingr_occur_map.values()))

    print("Part 1 Solution:", answer)

    for f in foods:
        f.ing -= not_allergens

    eng_candidate_map = {a: None for a in allergens}

    for a in allergens:
        ingr_sets = []
        for f in foods:
            if a in f.allerg:
                ingr_sets.append(f.ing)
        if len(ingr_sets) > 1:
            intersection = ingr_sets[0].intersection(*ingr_sets[1:])
        else:
            intersection = ingr_sets[0]

        eng_candidate_map[a] = intersection

    eng_gib_map = {a: None for a in allergens}
    not_processed = set(allergens)
    while eng_candidate_map:
        for a, gibs in eng_candidate_map.items():
            if len(gibs) == 1:
                break
        eng_gib_map[a] = list(gibs)[0]
        del eng_candidate_map[a]
        for a in eng_candidate_map:
            eng_candidate_map[a] -= gibs
        
    print(eng_gib_map)

    gib_eng_map = {
        gib: eng for eng, gib in eng_gib_map.items()
    }
    dang_list = list(eng_gib_map.values())
    dang_list.sort(key=lambda x: gib_eng_map[x])

    print("Part 2 solution:", ','.join(dang_list))
