from collections import deque

SIZE = 71
NUM_BYTES = 1024

grid = [["."] * SIZE for _ in range(SIZE)]
more_bytes = []

with open("input.txt") as f:
    i = 0
    for line in f:
        x, y = map(int, line.split(","))
        if i < NUM_BYTES:
            grid[y][x] = "#"
        else:
            more_bytes.append((x, y))
        i += 1

for byte_x, byte_y in more_bytes:
    grid[byte_y][byte_x] = "#"
    q = deque([(0, 0)])
    visited = set()
    reachable = False
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if {x, y} == {SIZE - 1}:
                q = deque()
                reachable = True
                break
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < SIZE and 0 <= ny < SIZE and grid[ny][nx] == ".":
                    q.append((nx, ny))
    if not reachable:
        print(f"{byte_x},{byte_y}")
        break
