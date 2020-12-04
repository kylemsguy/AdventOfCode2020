with open("input.txt") as infile:
    input_data = infile.readlines()

input_lst = [int(num.strip()) for num in input_data]

found_nums = None
for i in range(len(input_lst)):
    for j in range(1, len(input_lst)):
        if input_lst[i] + input_lst[j] == 2020:
            found_nums = (input_lst[i], input_lst[j])

print(found_nums)
if found_nums:
    print(f"Product: {found_nums[0]*found_nums[1]}")