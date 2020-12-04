with open('input2.txt') as infile:
    batch = infile.readlines()

passports = []

required_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",  
]
valid_passports = 0
buffer = []
print(len(batch))
for line in batch:
    print('asdf', line)
    stripped_line = line.strip()
    # print(stripped_line)
    # print(stripped_line)
    print(stripped_line)
    if stripped_line:
        # print(stripped_line)
        buffer.append(stripped_line)
    else:
        print(test)
        valid = True
        result = ' '.join(buffer)
        for field in required_fields:
            if field not in result:
                valid = False
                break
        if valid:
            valid_passports += 1
        buffer.clear()

print(valid_passports)