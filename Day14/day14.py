

if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.readlines()

    nums = [int(line.strip()) for line in raw.split('\n') if line.strip()]
