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
    for dr, dc in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
        if track.get((r + dr, c + dc), 0) - track[(r, c)] >= 102:
            ans += 1
print(ans)
