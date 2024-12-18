from collections import deque

SIZE = 71
NUM_BYTES = 1024

grid = [["."] * SIZE for _ in range(SIZE)]

with open("input.txt") as f:
    for i in range(NUM_BYTES):
        x, y = map(int, f.readline().split(","))
        grid[y][x] = "#"

q = deque([(0, 0)])
visited = set()
d = 0
while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        if {x, y} == {SIZE - 1}:
            print(d)
            break
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE and grid[ny][nx] == ".":
                q.append((nx, ny))
    d += 1
