class Bag:
    def __init__(self, colour):
        """
        bags is a list of tuples with bag and number
        """
        self.colour = colour
        self.bags = []

    def __str__(self):
        return f"{self.colour} bag containing {self.bags}"

    def __repr__(self):
        return f"{self.colour} bag containing {self.bags}"

    def add_bag(self, bag, quantity):
        self.bags.append((bag, quantity))

    def get_bag_count(self):
        return sum([b.get_bag_count() * n for b, n in self.bags])

    def get_bag_type_count(self, colour):
        count = 0
        for bag, quantity in self.bags:
            # print(bag.colour, colour)
            if bag.colour == colour:
                count += quantity
            count += bag.get_bag_type_count(colour) * quantity
        return count


def get_bag(bags, colour):
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

    # Build tree
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

    # print(bags)

    # Find number of bags that contain shiny gold bag
    contains_count = 0
    for colour in bags:
        bag = bags[colour]

        num_shiny_gold = bag.get_bag_type_count("shiny gold")
        # if num_shiny_gold:
        #     print(num_shiny_gold)

        if num_shiny_gold > 0:
            contains_count += 1

    print(contains_count)