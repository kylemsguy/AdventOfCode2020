if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    nums = [int(line.strip()) for line in raw.split('\n') if line.strip()]

    target = 41682220
    for i in range(len(nums)-1):
        curr_range = []
        the_sum = nums[i]
        for j in range(i+1, len(nums)):
            the_sum += nums[j]
            curr_range.append(nums[j])
            if the_sum == target:
                print(min(curr_range)+max(curr_range))
                exit(0)