if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    nums = [int(line.strip()) for line in raw.split('\n') if line.strip()]

    for i in range(25, len(nums)-25):
        found = False
        for j in range(i-25, i):
            for k in range(j+1, i+25):
                if nums[i] == nums[j] + nums[k]:
                    found = True
                    break
                if found:
                    break
            if found:
                break
        if not found:
            print("Not found", i, nums[i])
            break