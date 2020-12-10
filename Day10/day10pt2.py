class JoltAdapter:
    def __init__(self, num):
        self.num = num
        self.ways_to_reach = 0

    def __repr__(self):
        return f"{self.num}: waystoreach: {self.ways_to_reach}"


def count_paths(adapters_list):
    # This step is necessary
    adapters_list.sort()

    # Initialize JoltAdapter objects, including outlet and laptop
    adapters = [JoltAdapter(0)] + [JoltAdapter(x) for x in adapters_list] + [JoltAdapter(nums[-1] + 3)]

    # Initialize the root node to have 1 way to reach, or else the algorithm doesn't work
    adapters[0].ways_to_reach = 1

    # Convenient way to get adapters from nums
    # Could probably skip the previous list, and use num_adapter_map.values(), but whatever
    num_adapter_map = {n.num: n for n in adapters}

    # Go through the adapters and update the ways_to_reach values accordingly
    for node in adapters:
        for i in range(1, 4):
            if node.num + i in num_adapter_map:
                n = num_adapter_map[node.num + i]
                n.ways_to_reach += node.ways_to_reach

    # Return the ways to reach the last adapter (built-in to the laptop)
    return adapters[-1].ways_to_reach


if __name__ == "__main__":
    # Ingest the input
    with open("input.txt") as infile:
        raw = infile.read()

    nums = [int(line.strip()) for line in raw.split('\n') if line.strip()]
    
    # Print the solution
    print(count_paths(nums))
    