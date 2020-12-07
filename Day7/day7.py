class Bag:
    def __init__(self, colour):
        """A node representing a Bag and its contents

        Args:
            colour (str): The colour/description of the bag
        
        Instance Vars:
            bags (list(tuple)): A list of tuples bag (Bag), quantity (int) that represents 
                how much of the bag is contained within the current coloured Bag
        """
        self.colour = colour
        self.bags = []

    def __str__(self):
        return f"{self.colour} bag containing {self.bags}"

    def __repr__(self):
        return f"{self.colour} bag containing {self.bags}"

    def add_bag(self, bag, quantity):
        """Adds a required bag to the bag's contents

        Args:
            bag (Bag): The bag object to be added
            quantity (int): The quantity of bag that must be in self
        """
        self.bags.append((bag, quantity))

    def get_bag_count(self):
        """Calculates and returns how many bags need to be in the current bag.

        Returns:
            int: The number of bags within the current bag
        """
        # b.get_bag_count() + 1 because get_bag_count does not count itself
        # A bag does not contain itself for our purposes.
        return sum([(b.get_bag_count() + 1) * n for b, n in self.bags])

    def get_bag_type_count(self, colour):
        """Recursively calculates and returns how many bags of a certain colour 
            must be in the current bag.

        Args:
            colour (str): The bag's colour/description

        Returns:
            int: The number of bags with colour are contained in self
        """
        count = 0
        for bag, quantity in self.bags:
            # This gets around the need to count oneself
            if bag.colour == colour:
                count += quantity
            count += bag.get_bag_type_count(colour) * quantity
        return count


def get_bag(bags, colour):
    """Finds or creates a Bag with the requested colour/type
       If the colour/bag does not exist in bags, a new Bag is 
        created and added to bags

    Args:
        bags (dict(str: Bag)): A dict mapping colour to Bag objects
        colour (str): Colour/type of bag requested

    Returns:
        Bag: The Bag with the requested colour contained within bags
    """
    if colour in bags:
        bag = bags[colour]
    else:
        bag = Bag(colour)
        bags[colour] = bag
    return bag


if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    lines = [line.strip() for line in raw.split('\n')]

    bags = {}

    # Build tree of bags
    for line in lines:
        if not line:
            continue
        colour, contents = line.split("contain")
        contents = contents.strip()
        colour = ' '.join(colour.strip().split(' ')[:-1])
        bag = get_bag(bags, colour)
        
        if contents != 'no other bags.':
            descriptors = [c.strip() for c in contents.split(",")]
            for d in descriptors:
                parts = d.split(' ')
                quantity = int(parts[0])
                child_colour = ' '.join(parts[1:-1])

                child_bag = get_bag(bags, child_colour)
                bag.add_bag(child_bag, quantity)

    # Part 1: Find number of bags that contain shiny gold bag
    my_bag = "shiny gold"
    contains_count = 0
    for colour in bags:
        bag = bags[colour]

        num_shiny_gold = bag.get_bag_type_count(my_bag)
        # if num_shiny_gold:
        #     print(num_shiny_gold)

        if num_shiny_gold > 0:
            contains_count += 1

    print(f"Part 1 (number of bags that contain {my_bag} bags):")
    print(contains_count)

    # Part 2: Find number of bags inside my bag
    print(f"Part 2 (number of bags contained within my {my_bag} bag):")
    print(bags[my_bag].get_bag_count())
