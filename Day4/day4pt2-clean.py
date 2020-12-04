import re

def validate_year(value, start, end):
    if len(value) != 4:
        return False
    try:
        year = int(value)
    except ValueError:
        return False

    return year >= start and year <= end

def validate_height(value, min, max):
    if len(value) < 3:
        return False
    try:
        height = int(value[:-2])
    except ValueError:
        return False

    return height >= min and height <= max

def validate_num(value, length):
    if len(value) != length:
        return False
    
    try:
        num = int(value)
    except ValueError:
        return False

    return True


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
            do_print = False
            valid = False
            break
        if field == 'byr':
            valid = validate_year(passport[field], 1920, 2002)
        elif field == 'iyr':
            valid = validate_year(passport[field], 2010, 2020)
        elif field == 'eyr':
           valid = validate_year(passport[field], 2020, 2030)
        elif field == 'hgt':
            val = passport[field]
            if val[-2:] == 'cm':
                valid = validate_height(val, 150, 193)
            elif val[-2:] == 'in':
                valid = validate_height(val, 59, 76)
            else:
                valid = False
        elif field == 'hcl':
            valid = re.match("\#[0-9a-f]{6}", passport[field]) is not None
        elif field == 'ecl':
            valid = passport[field] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        elif field == 'pid':
            valid = validate_num(passport[field], 9)

        if not valid:
            print("failed on", field)
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