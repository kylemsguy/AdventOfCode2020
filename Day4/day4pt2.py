import re

with open('input.txt') as infile:
    batch = infile.readlines()

passports = []

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

curr_passport = {}
for line in batch:
    stripped_line = line.strip()
    if not stripped_line:
        passports.append(curr_passport)
        curr_passport = {}
        continue
    kv = stripped_line.split(' ')
    for item in kv:
        key, val = item.split(':')
        curr_passport[key] = val
passports.append(curr_passport)

valid_passports = 0
for passport in passports:
    do_print = True
    valid = True
    for field in required_fields:
        if field not in passport:
            # print(len(passport))
            # print(passport)
            # print(field, 'not present')
            do_print = False
            valid = False
            break
        if field == 'byr':
            if len(passport[field]) != 4:
                valid = False
                break
            try:
                year = int(passport[field])
            except ValueError:
                valid = False
                break
            if year < 1920 or year > 2002:
                valid = False
                break
        elif field == 'iyr':
            if len(passport[field]) != 4:
                valid = False
                break
            try:
                year = int(passport[field])
            except ValueError:
                valid = False
                break
            if year < 2010 or year > 2020:
                valid = False
                break
        elif field == 'eyr':
            try:
                year = int(passport[field])
            except ValueError:
                valid = False
                break
            if year < 2020 or year > 2030:
                valid = False
                break
        elif field == 'hgt':
            if (match := re.match("[0-9]+cm", passport[field])):
                h = int(passport[field][:-2])
                if h < 150 or h > 193:
                    valid = False
                    break
            elif (match := re.match("[0-9]+in", passport[field])):
                h = int(passport[field][:-2])
                if h < 59 or h > 76:
                    valid = False
                    break 
            else:
                valid = False
                break
                
        elif field == 'hcl':
            if not re.match("\#[0-9a-f]{6}", passport[field]):
                valid = False
                break
        elif field == 'ecl':
            if passport['ecl'] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                valid = False
                break
        elif field == 'pid':
            if not re.match("[0-9]{9}", passport['pid']):
                valid = False
                break
    if valid:
        print("{", end='')
        for k in sorted(list(passport.keys())):
            if k == 'cid': continue
            print(f"{k}: {passport[k]}, ", end='')
        print("}")
        valid_passports += 1
    # elif do_print:
    #     print(field)
    #     print(passport)


print(valid_passports)