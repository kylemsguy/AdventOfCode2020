class Node:
    def __init__(self, num):
        self.num = num
        self.next = []
        self.ways_to_reach = 0

    def __repr__(self):
        return f"{self.num}: waystoreach: {self.ways_to_reach}"

def count_permutations(nums):
    nodes = [Node(0)] + [Node(x) for x in nums] + [Node(nums[-1] + 3)]
    nodes[0].ways_to_reach = 1
    num_node_map = {n.num: n for n in nodes}

    for node in nodes:
        if node.num == 172:
            print()
            pass
        for i in range(1, 4):
            if node.num + i in num_node_map:
                n = num_node_map[node.num + i]
                node.next.append(n)
                n.ways_to_reach += node.ways_to_reach

    return nodes[-1].ways_to_reach


if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    nums = [int(line.strip()) for line in raw.split('\n') if line.strip()]

    nums.sort()
    
    print(count_permutations(nums))