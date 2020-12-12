import math


quadrant_coefficient = {
    1: (1,1),
    2: (-1,1),
    3: (-1,-1),
    4: (1,-1),
}


# def get_quadrant(pos):
#     x, y = pos
#     if x >= 0 and y >= 0:
#         return 1
#     elif x < 0 and y >= 0:
#         return 2
#     elif x < 0 and y < 0:
#         return 3
#     elif x >= 0 and y < 0:
#         return 4

# def move_to_quadrant(pos, angle):
#     x, y = pos
#     quadrant = get_quadrant(pos)
#     new_quadrant = (quadrant + int(angle / 90) - 1) % 4 + 1
#     # print(quadrant, new_quadrant)

#     x_c, y_c = quadrant_coefficient[new_quadrant]
#     return abs(x) * x_c, abs(y) * y_c



def rotate(pos, ins):
    x, y = pos
    amount = int(ins[1:])
    if ins[0] == 'R':
        amount = -1 * amount
    rad = math.radians(amount)

    length = math.sqrt(x**2 + y**2)
    if y == 0:
        if x > 0:
            angle = 0
        elif x < 0:
            angle = 180
        else:
            return x, y
    else:
        angle = (y / abs(y)) * math.degrees(math.acos(x / length))

    new_angle = angle + amount

    new_x = length * math.cos(math.radians(angle + amount))
    new_y = length * math.sin(math.radians(angle + amount))

    return round(new_x), round(new_y)


# def rotate(pos, ins):
#     x, y = pos
#     amount = int(ins[1:])
#     if ins[0] == 'R':
#         amount = -1 * amount
    
#     return move_to_quadrant(pos, amount)

def move(pos, waypoint, ins):
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
    # filename = "input_small.txt"
    with open(filename) as infile:
        raw = infile.read()

    # Already filters any empty lines
    directions = [line for line in raw.split('\n') if line.strip()]

    pos = 0, 0

    waypoint = 10, 1

    print(rotate((10, 4), 'R90'))
    
    for d in directions:
        if d[0] in ["N","S","E","W","F"]:
            pos, waypoint = move(pos, waypoint, d)
        else:
            waypoint = rotate(waypoint, d)
        print(d, pos, waypoint)

    x, y = pos
    print(abs(x) + abs(y))