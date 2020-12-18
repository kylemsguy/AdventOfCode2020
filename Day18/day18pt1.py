# The smart way might be to build an AST...


def eval_expr(line):
    # if slicing, add 1 to end
    outer_parens = []
    paren_count = 0
    paren_start = None

    # Find top-level parens
    for i, char in enumerate(line):
        if char == '(':
            paren_count += 1
            if paren_start is None:
                paren_start = i
        elif char == ')':
            paren_count -= 1
            if paren_count == 0:
                outer_parens.append((paren_start, i))
                paren_start = None

    # Recursively evaluate all top-level parens
    if outer_parens:
        startend_vals = {}
        for start, end in outer_parens:
            # Recursively evaluate expr in parens
            val = eval_expr(line[start+1:end])
            startend_vals[(start, end)] = val

        curr = 0
        # if slicing, add 1 to end
        parts = []
        for start, end in outer_parens:
            if start != 0:
                parts.append(line[curr: start])
            parts.append(str(startend_vals[(start, end)]))
            if (curr := end + 1) >= len(line):
                break

        if curr < len(line):
            parts.append(line[curr:])

        new_line = ''.join(parts)
        parts = new_line.split(' ')
    else:
        # If there are no parens, just split normally
        parts = line.split(' ')

    # Evaluate all remaining operations
    i = 1
    prev_val = int(parts[0])
    # Skip the loop if all we have left is a single value
    while i < len(parts):
        next_val = int(parts[i+1])
        op = parts[i]
        if op == '+':
            prev_val += next_val
        elif op == '*':
            prev_val *= next_val
        else:
            print("ERROR", op, i)
            raise ValueError
        i += 2

    return prev_val
    


if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    print(eval_expr("(5 * 7 * 5) * 6 * 5 + 7 + 6 * 4"))

    lines = [line for line in raw.split('\n') if line.strip()]

    answer = 0
    for line in lines:
        answer += eval_expr(line)

    print(answer)