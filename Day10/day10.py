if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    nums = [line.strip() for line in raw.split('\n') if line.strip()]
