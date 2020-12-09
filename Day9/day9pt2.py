if __name__ == "__main__":
    print("Note: any line numbers are 1-indexed")
    print()
    with open("input.txt") as infile:
        raw = infile.read()

    nums = [int(line.strip()) for line in raw.split('\n') if line.strip()]

    # Copied from the output of day9.py
    target = 41682220
    # Search the entire range, except for the last number (since seq length >= 2)
    for i in range(len(nums)-1):
        curr_range = []
        the_sum = nums[i]
        # Add every number until the end of the file
        for j in range(i+1, len(nums)):
            the_sum += nums[j]
            # Keep track of the sequence
            curr_range.append(nums[j])
            # If we've found a matching sequence
            if the_sum == target:
                print("We've found a matching sequence")
                print(f"Starting line: {i+1}, ending line: {j+1}")
                # Get the min and max of the sequence, and print the sum
                print("Sum of min and max:", min(curr_range) + max(curr_range))

                # I guess exit will do for jumping out of the nested loops
                exit(0)
