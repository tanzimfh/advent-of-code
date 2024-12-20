grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))


def find(r, c):
    if (r, c) in visited:
        return 0
    visited.add((r, c))

    per = 4
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r2, c2 = r + dr, c + dc
        if (
            0 <= r2 < len(grid)
            and 0 <= c2 < len(grid[r2])
            and grid[r2][c2] == grid[r][c]
        ):
            per += find(r2, c2) - 1
    return per


ans = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == ".":
            continue
        visited = set()
        per = find(r, c)
        ans += per * (len(visited))
        for r2, c2 in visited:
            grid[r2][c2] = "."
print(ans)
