grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))


def find(r, c):
    if (r, c) in visited:
        return 0
    char = grid[r][c]
    per = 0
    borders = [False] * 4
    # find if cell has top, bottom, left, right borders
    if r == 0 or grid[r - 1][c] != char:
        borders[0] = True
        per += 1
    if r == len(grid) - 1 or grid[r + 1][c] != char:
        borders[1] = True
        per += 1
    if c == 0 or grid[r][c - 1] != char:
        borders[2] = True
        per += 1
    if c == len(grid[r]) - 1 or grid[r][c + 1] != char:
        borders[3] = True
        per += 1
    visited[(r, c)] = borders
    # decrement per for each border shared by a visited neighbor
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r2, c2 = r + dr, c + dc
        if 0 <= r2 < len(grid) and 0 <= c2 < len(grid[r2]) and (r2, c2) in visited:
            other_borders = visited[(r2, c2)]
            if c == c2:
                per -= int(borders[2] and other_borders[2])
                per -= int(borders[3] and other_borders[3])
            else:
                per -= int(borders[1] and other_borders[1])
                per -= int(borders[0] and other_borders[0])

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r2, c2 = r + dr, c + dc
        if 0 <= r2 < len(grid) and 0 <= c2 < len(grid[r2]) and grid[r2][c2] == char:
            per += find(r2, c2)
    return per


ans = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == ".":
            continue
        visited = {}
        per = find(r, c)
        ans += per * (len(visited))
        for r2, c2 in visited:
            grid[r2][c2] = "."
print(ans)
