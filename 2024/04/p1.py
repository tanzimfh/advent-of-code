grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

ans = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):

        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if all(
                    0 <= r + dr * i < len(grid)
                    and 0 <= c + dc * i < len(grid[0])
                    and grid[r + dr * i][c + dc * i] == "XMAS"[i]
                    for i in range(4)
                ):
                    ans += 1
print(ans)
