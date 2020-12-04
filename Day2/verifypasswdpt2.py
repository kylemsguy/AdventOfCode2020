with open("input.txt") as infile:
    input_data = infile.readlines()

passwords = []
for item in input_data:
    r, l, pwd = item.strip().split(' ')
    min_occur, max_occur = r.split('-')
    letter = l.strip(':')

    passwords.append((int(min_occur), int(max_occur), letter, pwd))

valid_count = 0
for min_occur, max_occur, letter, pwd in passwords:
    valid = False
    if (pwd[min_occur-1] == letter and pwd[max_occur-1] != letter) or (pwd[min_occur-1] != letter and pwd[max_occur-1] == letter):
        valid = True
        valid_count += 1

    print(f"{min_occur}-{max_occur} {letter}: {pwd} - valid: {valid}")

print(f"Number of valid passwords: {valid_count}")
print(f"Number of invalid passwords: {len(passwords)-valid_count}")
