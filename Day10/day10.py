if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    nums = [int(line.strip()) for line in raw.split('\n') if line.strip()]

    # This step is necessary
    nums.sort()

    # Both initially set to 1 because outlet = 0, first adapter is 1, and cpu = max+3
    one_diff = 1
    three_diff = 1

    # print(nums)

    for i in range(len(nums)-1):
        j = i + 1
        if nums[j] - nums[i] == 1:
            one_diff += 1
        elif nums[j] - nums[i] == 3:
            three_diff += 1
        elif nums[j] - nums[i] > 3:
            # This should not happen unless input is bad
            print("BAD")
            print(nums[j] - nums[i])
    
    print("Part One solution:", one_diff * three_diff)
