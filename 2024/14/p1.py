robots = []
with open("input.txt") as f:
    for line in f:
        p, v = line.split(" ")
        px, py = map(int, p[2:].split(","))
        vx, vy = map(int, v[2:].split(","))
        robots.append([px, py, vx, vy])

SPACE_X, SPACE_Y = 101, 103

q1, q2, q3, q4 = 0, 0, 0, 0
for px, py, vx, vy in robots:
    for i in range(100):
        px += vx
        py += vy
        px = (SPACE_X + px) % SPACE_X
        py = (SPACE_Y + py) % SPACE_Y
    if px < SPACE_X // 2:
        if py < SPACE_Y // 2:
            q1 += 1
        elif py > SPACE_Y // 2:
            q2 += 1
    elif px > SPACE_X // 2:
        if py < SPACE_Y // 2:
            q3 += 1
        elif py > SPACE_Y // 2:
            q4 += 1
print(q1 * q2 * q3 * q4)
