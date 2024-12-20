antennas = {}
with open("input.txt") as f:
    r = 0
    for line in f:
        line = line.strip()
        len_grid_0 = len(line)
        for c, char in enumerate(line):
            if char != ".":
                antennas[char] = antennas.get(char, []) + [(r, c)]
        r += 1
    len_grid = r


def add_valid(r, c):
    if 0 <= r < len_grid and 0 <= c < len_grid_0:
        antinodes.add((r, c))


antinodes = set()
for locations in antennas.values():
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            r1, c1 = locations[i]
            r2, c2 = locations[j]

            dr, dc = r2 - r1, c2 - c1

            add_valid(r1 - dr, c1 - dc)
            add_valid(r2 + dr, c2 + dc)
print(len(antinodes))
