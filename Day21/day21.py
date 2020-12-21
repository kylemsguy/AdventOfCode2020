import re
import math
import itertools
import numpy as np
from collections import defaultdict

class Food:
    def __init__(self, ingredients, allergens):
        self.ing = set(ingredients)
        self.allerg = set(allergens)


def update_probable_allergens(probable_allergens, food1, food2):
    common_ingrs = food1.ing.intersection(food2.ing)
    if food1.allerg.intersection(food2.allerg):
        probable_allergens.update(common_ingrs)
    else:
        # What do we do here?
        pass

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

    # could_allergens = set()
    # for i in range(len(foods)-1):
    #     for j in range(i+1, len(foods)):
    #         food1, food2 = foods[i], foods[j]
    #         update_probable_allergens(could_allergens, food1, food2)
    #         # could_allergens.update(allergens)

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
