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

if __name__ == "__main__":
    with open("nearby.txt") as infile:
        raw = infile.readlines()

    tickets = []
    for line in raw:
        split = line.strip().split(',')
        t = [int(f) for f in split]    
        tickets.append(t)

    my_ticket = [61,151,59,101,173,71,103,167,127,157,137,73,181,97,179,149,131,139,67,53]

    invalid_count = 0
    for ticket in tickets:
        for field in ticket:
            has_valid = False
            for r in rules:
                if check_any_valid(field, rules[r]):
                    has_valid = True
                    break
            invalid_count += field if not has_valid else 0
    
    print(invalid_count)