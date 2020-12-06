with open("input.txt") as infile:
    raw = infile.read()

lines = [line.strip() for line in raw.split('\n')]

groups = []
current_group = set()
for line in lines:
    if not line:
        groups.append(current_group)
        current_group = set()
    else:
        for char in line:
            current_group.add(char)

group_counts = [len(x) for x in groups]

# print(group_counts)
print(sum(group_counts))