grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(map(int, list(line.strip()))))


def dfs(r, c):
    if grid[r][c] == 9:
        reachable.add((r, c))
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (
            0 <= r + dr < len(grid)
            and 0 <= c + dc < len(grid[0])
            and grid[r + dr][c + dc] == grid[r][c] + 1
        ):
            dfs(r + dr, c + dc)


ans = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 0:
            reachable = set()
            dfs(r, c)
            ans += len(reachable)
print(ans)
