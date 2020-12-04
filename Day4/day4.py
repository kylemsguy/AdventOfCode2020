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
    valid = True
    for field in required_fields:
        if field not in passport:
            valid = False
            break
    if valid:
        valid_passports += 1

print(valid_passports)