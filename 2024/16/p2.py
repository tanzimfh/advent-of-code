from collections import deque

grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))
        if "S" in line:
            start = (len(grid) - 1, line.index("S"))
        elif "E" in line:
            end = (len(grid) - 1, line.index("E"))

N, S, E, W = (-1, 0), (1, 0), (0, 1), (0, -1)
q = deque([(start, E)])
dist = {(start, E): 0}
path = {start: {0: {start}}}

while q:
    (r, c), (dr, dc) = q.popleft()
    for ndr, ndc in [N, S, E, W]:
        nr, nc = r + ndr, c + ndc
        turn_cost = 1000 * max(abs(ndr - dr), abs(ndc - dc))
        new_dist = dist[((r, c), (dr, dc))] + 1 + turn_cost

        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != "#":
            if (nr, nc) not in path:
                path[(nr, nc)] = {}
                path[(nr, nc)][new_dist] = path[(r, c)][dist[((r, c), (dr, dc))]].union(
                    {(nr, nc)}
                )
            else:
                path[(nr, nc)][new_dist] = (
                    path[(nr, nc)]
                    .get(new_dist, set())
                    .union(path[(r, c)][dist[((r, c), (dr, dc))]])
                )
            path[(nr, nc)][new_dist].add((nr, nc))

            if new_dist < dist.get(((nr, nc), (ndr, ndc)), float("inf")):
                dist[((nr, nc), (ndr, ndc))] = new_dist
                q.append(((nr, nc), (ndr, ndc)))

print(len(path[end][min(path[end])]))
