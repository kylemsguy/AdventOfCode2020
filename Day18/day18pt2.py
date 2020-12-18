import numpy as np


def eval_expr(line):
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
        parts = line.split(' ')

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

    i = 1
    prev_val = int(parts[0])
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

    print(eval_expr("9 + (8 * 5 * 5 * 4 * (3 * 5) * 2) + 4 + 4"))

    lines = [line for line in raw.split('\n') if line.strip()]

    answer = 0
    for line in lines:
        answer += eval_expr(line)

    print(answer)