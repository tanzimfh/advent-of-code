grid = []
with open('input.txt') as f:
    for line in f:
        grid.append(list(line.strip()))
        if '^' in line:
            start_r, start_c = len(grid) - 1, line.index('^')

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ans = 0
for obstruction_r in range(len(grid)):
    for obstruction_c in range(len(grid[0])):
        if grid[obstruction_r][obstruction_c] == '#':
            continue
        grid[obstruction_r][obstruction_c] = '#'
        visited = set()
        r, c = start_r, start_c
        di = 0
        while True:
            if (r, c, di) in visited:
                ans += 1
                break
            visited.add((r, c, di))
            dr, dc = directions[di]
            nr, nc = r + dr, c + dc
            if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]):
                break
            if grid[nr][nc] == '#':
                di = (di + 1) % 4
                continue
            r, c = nr, nc
        grid[obstruction_r][obstruction_c] = '.'
print(ans)