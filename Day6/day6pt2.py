from collections import defaultdict
with open("input.txt") as infile:
    raw = infile.read()

lines = [line.strip() for line in raw.split('\n')]

groups = []
current_group_count = 0
current_group = defaultdict(int)
for line in lines:
    if not line:
        res = len([x for x in current_group if current_group[x] == current_group_count])
        groups.append(res)
        current_group = defaultdict(int)
        current_group_count = 0
    else:
        current_group_count += 1
        for char in line:
            current_group[char] += 1

print(sum(groups))