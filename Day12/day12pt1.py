import math

angle_direction_map = {
    0: 'N',
    90: 'E',
    180: 'S',
    270: 'W',
}
direction_angle_map = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270,
}


def rotate(angle, ins):
    amount = int(ins[1:])
    if ins[0] == 'L':
        amount = -1 * amount
    return (angle + amount) % 360


def move(pos, facing, ins):
    # Note: Part 1 uses screen coords
    # This means N is -y and S is +y
    x, y = pos
    amount = int(ins[1:])
    direction = ins[0]
    if direction == 'F':
        direction = angle_direction_map[facing]
    elif direction == 'R':
        facing = (facing + 180) % 360
        direction = angle_direction_map[facing]
    if direction == 'N':
        y -= amount
    elif direction == 'E':
        x += amount
    elif direction == 'S':
        y += amount
    elif direction == 'W':
        x -= amount

    return x, y


if __name__ == "__main__":
    with open("input.txt") as infile:
        raw = infile.read()

    # Already filters any empty lines
    directions = [line for line in raw.split('\n') if line.strip()]

    x = 0
    y = 0
    angle = 90
    
    for d in directions:
        if d[0] in ["N","S","E","W","F"]:
            x, y = move((x,y), angle, d)
        else:
            angle = rotate(angle, d)
        print(d, x, y, angle)

    print("Part 1 Manhatten distance:", abs(x) + abs(y))