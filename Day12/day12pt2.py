import math


def rotate(pos, ins):
    x, y = pos
    amount = int(ins[1:])
    if ins[0] == 'R':
        amount = -1 * amount
    rad = math.radians(amount)

    length = math.sqrt(x*x + y*y)
    angle = math.degrees(math.atan2(y, x))

    new_angle = angle + amount

    new_x = length * math.cos(math.radians(angle + amount))
    new_y = length * math.sin(math.radians(angle + amount))

    return round(new_x), round(new_y)


def move(pos, waypoint, ins):
    # Note: for part 2 we are using traditional cartesian coords
    # This means that 'N' is +y and 'S' is -y
    x, y = pos
    x_w, y_w = waypoint
    amount = int(ins[1:])
    direction = ins[0]

    if direction == 'F':
        x += x_w * amount
        y += y_w * amount
    if direction == 'N':
        y_w += amount
    elif direction == 'E':
        x_w += amount
    elif direction == 'S':
        y_w -= amount
    elif direction == 'W':
        x_w -= amount

    return (x, y), (x_w, y_w)


if __name__ == "__main__":
    filename = "input.txt"
    with open(filename) as infile:
        raw = infile.read()

    # Already filters any empty lines
    directions = [line for line in raw.split('\n') if line.strip()]

    pos = 0, 0

    waypoint = 10, 1

    for d in directions:
        if d[0] in ["N","S","E","W","F"]:
            pos, waypoint = move(pos, waypoint, d)
        else:
            waypoint = rotate(waypoint, d)
        # print(d, pos, waypoint)

    x, y = pos
    print("Part 2 Manhatten distance:", abs(x) + abs(y))