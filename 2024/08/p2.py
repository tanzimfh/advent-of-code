from fractions import Fraction

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

antinodes = set()
for locations in antennas.values():
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            r1, c1 = locations[i]
            r2, c2 = locations[j]

            dr, dc = r2 - r1, c2 - c1

            if dc == 0:
                dr = 1
            else:
                f = Fraction(dr, dc)
                dr, dc = f.numerator, f.denominator

            while 0 <= r1 < len_grid and 0 <= c1 < len_grid_0:
                antinodes.add((r1, c1))
                r1 += dr
                c1 += dc
            while 0 <= r2 < len_grid and 0 <= c2 < len_grid_0:
                antinodes.add((r2, c2))
                r2 -= dr
                c2 -= dc
print(len(antinodes))
