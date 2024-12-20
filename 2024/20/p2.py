from collections import deque

grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))
        if "S" in line:
            start = (len(grid) - 1, line.index("S"))

track = {}
steps = 0
r, c = start
while True:
    grid[r][c] = "X"
    track[(r, c)] = steps
    steps += 1
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (
            0 <= r + dr < len(grid)
            and 0 <= c + dc < len(grid[0])
            and grid[r + dr][c + dc] in {".", "E"}
        ):
            r += dr
            c += dc
            break
    else:
        break

ans = 0
for r, c in track:
    q = deque([(r, c)])
    visited = set()
    for d in range(21):
        for _ in range(len(q)):
            r2, c2 = q.popleft()
            if (
                (r2, c2) in visited
                or not 0 <= r2 < len(grid)
                or not 0 <= c2 < len(grid[0])
            ):
                continue
            visited.add((r2, c2))
            if track.get((r2, c2), 0) - track.get((r, c), float("inf")) >= (100 + d):
                ans += 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                q.append((r2 + dr, c2 + dc))
print(ans)
