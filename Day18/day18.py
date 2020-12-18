# A smarter way might have been to build an AST
# This is what I came up with first.

# The difference between Part 1 and Part 2 was just one
# pre-processing step, so combining them into one function
# was pretty easy.

# The preprocessing steps were not broken into separate functions
# for legibility's sake (no need to scroll up/down to func def)


def eval_expr(line, add_first=False):
    """Evaluates an expression via AoC2020Day18 Rules

    Args:
        line (str): The expression to be evaluated (1 line of input)
        add_first (bool, optional): whether to evaluate '+' first. Defaults to False.

    Raises:
        ValueError: Something went wrong; added only for debugging

    Returns:
        int: The value of the expression
    """
    # if slicing, add 1 to end
    outer_parens = []
    paren_count = 0
    paren_start = None
    # Find outer parens
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

    if add_first:
        # Evaluate and consume all '+' ops first, if any
        # If we just have a single op, skip this step
        if len(parts) > 3:
            new_parts = []
            # eval + first
            i = 0
            prev_val = None
            while i + 2 < len(parts):
                lhs = int(parts[i]) if prev_val is None else prev_val
                op = parts[i+1]
                rhs = int(parts[i+2])

                if op == '+':
                    prev_val = lhs + rhs
                else:
                    new_parts.append(str(lhs))
                    new_parts.append(op)
                    prev_val = None
                i += 2
            if prev_val is not None:
                new_parts.append(str(prev_val))
            if op == '*':
                new_parts.append(parts[-1])
            old_parts = parts
            parts = new_parts

    # Evaluate remaining operations
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

    lines = [line for line in raw.split('\n') if line.strip()]

    answer_pt1 = 0
    for line in lines:
        answer_pt1 += eval_expr(line)

    print("Part 1:", answer_pt1)

    answer_pt2 = 0
    for line in lines:
        answer_pt2 += eval_expr(line, add_first=True)

    print("Part 2:", answer_pt2)