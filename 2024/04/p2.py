grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

ans = 0
for r in range(1, len(grid) - 1):
    for c in range(1, len(grid[0]) - 1):
        if grid[r][c] == "A":
            if {grid[r - 1][c - 1], grid[r + 1][c + 1]} == {"M", "S"}:
                if {grid[r + 1][c - 1], grid[r - 1][c + 1]} == {"M", "S"}:
                    ans += 1
print(ans)
