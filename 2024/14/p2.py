robots = []
with open("input.txt") as f:
    for line in f:
        p, v = line.split(" ")
        px, py = map(int, p[2:].split(","))
        vx, vy = map(int, v[2:].split(","))
        robots.append([px, py, vx, vy])

SPACE_X, SPACE_Y = 101, 103

i = 1
while True:
    locs = set()
    for robot in robots:
        robot[0] = (SPACE_X + robot[0] + robot[2]) % SPACE_X
        robot[1] = (SPACE_Y + robot[1] + robot[3]) % SPACE_Y
        locs.add((robot[0], robot[1]))
    # look for horizontal line of robots
    for r in range(SPACE_X):
        count = 0
        for c in range(SPACE_Y):
            if (r, c) in locs:
                count += 1
            else:
                count = 0
            if count > 16:
                print(i)
                exit()
    i += 1
