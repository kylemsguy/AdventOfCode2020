if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    nums = [int(line.strip()) for line in raw.split('\n') if line.strip()]

    # Search starting at the 26th number
    for i in range(25, len(nums)):
        found = False
        # Search the past 25 numbers
        for j in range(i-25, i):
            # and add each of the next 24 numbers
            for k in range(j+1, i):
                # if we've found a sum that matches
                if nums[i] == nums[j] + nums[k]:
                    # Stop here, and mark as valid
                    found = True
                    break
                # I wish there was a better way to jump out of nested loops...
                if found:
                    break
            # maybe a goto, like in C? Or maybe make a function and return...
            if found:
                break
        # We've found the number we were looking for
        if not found:
            print("First number not meeting constraints:")
            print(f"line {i+1}: {nums[i]}")
            break