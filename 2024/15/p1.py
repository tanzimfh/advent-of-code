grid = []
moves = ""
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if "<" in line:
            moves += line
            continue
        if "@" in line:
            pr, pc = (len(grid), line.index("@"))
        grid.append(list(line))

direction = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

for i, move in enumerate(moves):
    dr, dc = direction[move]
    tr, tc = pr + dr, pc + dc

    while grid[tr][tc] != "#":
        if grid[tr][tc] == ".":
            break
        tr += dr
        tc += dc
    else:
        continue

    grid[tr][tc] = "O"
    grid[pr][pc] = "."
    pr += dr
    pc += dc
    grid[pr][pc] = "@"

ans = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "O":
            ans += 100 * r + c
print(ans)
