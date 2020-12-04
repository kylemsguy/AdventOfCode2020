with open("input.txt") as infile:
    input_data = infile.readlines()

input_lst = [int(num.strip()) for num in input_data]
for i in range(0, len(input_lst), 3):
    for j in range(1, len(input_lst), 2):
        for k in range(2, len(input_lst)):
            if input_lst[i] + input_lst[j] + input_lst[k] == 2020:
                print("Found:", input_lst[i], input_lst[j], input_lst[k])
                print("Product:", input_lst[i] * input_lst[j] * input_lst[k])
                break