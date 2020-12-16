from collections import defaultdict
import copy

rules = {
    "departure location": [[29,458], [484,956]],
    "departure station": [[40,723], [738,960]],
    "departure platform": [[30,759], [784,956]],
    "departure track": [[37,608], [623,964]],
    "departure date": [[31,664], [685,950]],
    "departure time": [[27,498], [508,959]],
    "arrival location": [[36,245], [269,961]],
    "arrival station": [[35,808], [814,973]],
    "arrival platform": [[40,831], [856,951]],
    "arrival track": [[36,857], [875,971]],
    "class": [[43,161], [167,963]],
    "duration": [[25,75], [91,966]],
    "price": [[37,708], [724,972]],
    "route": [[39,370], [396,971]],
    "row": [[47,280], [299,949]],
    "seat": [[41,105], [125,952]],
    "train": [[43,351], [359,966]],
    "type": [[34,575], [586,965]],
    "wagon": [[27,397], [420,953]],
    "zone": [[48,206], [226,965]],
}


def check_any_valid(num, ranges):
    for min_val, max_val in ranges:
        if num >= min_val and num <= max_val:
            return True
    return False


def check_multiple_valid(nums, ranges):
    for num in nums:
        is_valid = True
        for min_val, max_val in ranges:
            if num < min_val or num > max_val:
                is_valid = False
            else:
                is_valid = True
        if is_valid:
            break
    return is_valid


def ticket_is_valid(ticket):
    for field in ticket:
        has_valid = False
        for r in rules:
            if check_any_valid(field, rules[r]):
                has_valid = True
                break
        if not has_valid:
            return False
    return True


# def get_ranges(tickets, field_num):
#     min_val = 1e99
#     max_val = -1
#     for t in tickets:
#         val = t[field_num]
#         if val < min_val:
#             min_val = val
#         if val > max_val:
#             max_val = val
#     return min_val, max_val


def get_column(lsts, col):
    result = []
    for l in lsts:
        result.append(l[col])
    return result


def get_field_names(col):
    valid_field_names = []
    for f, r in rules.items():
        is_valid = True
        for c in col:
            if not check_any_valid(c, r):
                is_valid = False
                break
        if is_valid:
            valid_field_names.append(f)

    return valid_field_names

def find_actual_field_names(possible_fields):
    fields = copy.deepcopy(possible_fields)
    field_index_map = {}
    while len(field_index_map) < len(possible_fields):
        # get field with only one element
        field = None
        index = None
        for f, p in fields.items():
            if len(p) == 1:
                field = f
                index = p[0]
                break
        del fields[f]
        field_index_map[field] = index
        for f, p in fields.items():
            if index in p:
                fields[f].remove(index)
    return field_index_map

if __name__ == "__main__":
    with open("nearby.txt") as infile:
        raw = infile.readlines()

    tickets = []
    for line in raw:
        split = line.strip().split(',')
        t = [int(f) for f in split]    
        tickets.append(t)

    my_ticket = [61,151,59,101,173,71,103,167,127,157,137,73,181,97,179,149,131,139,67,53]

    valid_tickets = [t for t in tickets if ticket_is_valid(t)]
    to_check = valid_tickets + [my_ticket]

    field_index_map = defaultdict(list)
    for i in range(len(valid_tickets[0])):
        col = get_column(to_check, i)
        possible_field_names = get_field_names(col)
        for f in possible_field_names:
            field_index_map[f].append(i)

    # for t in valid_tickets:
    #     print(','.join([str(i) for i in t]))

    for k, v in field_index_map.items():
        print(f"{k}:{v}")
    
    actual_field_index_map = find_actual_field_names(field_index_map)

    result = 1
    for f in rules:
        if f.startswith('departure'):
            result *= my_ticket[actual_field_index_map[f]]

    print(result)
    