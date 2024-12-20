grid = []
with open('input.txt') as f:
    for line in f:
        grid.append(list(line.strip()))
        if '^' in line:
            r, c = len(grid) - 1, line.index('^')

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
di = 0

ans = 0
while True:
    if grid[r][c] != 'X':
        ans += 1
        grid[r][c] = 'X'
    dr, dc = directions[di]
    nr, nc = r + dr, c + dc
    if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]):
        break
    if grid[nr][nc] == '#':
        di = (di + 1) % 4
        continue
    r, c = nr, nc
print(ans)