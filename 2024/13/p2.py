import re

pattern = re.compile(
    r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
)
machines = []
with open("input.txt") as f:
    inp = f.read()
    for match in pattern.finditer(inp):
        machines.append(list(map(int, match.groups())))

ans = 0
for ax, ay, bx, by, px, py in machines:
    px += 10000000000000
    py += 10000000000000

    # (1) a * ax + b * bx = px -> a = (px - b * bx) / ax
    # (2) a * ay + b * by = py -> a = (py - b * by) / ay
    # (px - b * bx) / ax = (py - b * by) / ay
    # ay * (px - b * bx) = ax * (py - b * by)
    # ay * px - ay * b * bx = ax * py - ax * b * by
    # ay * px - ax * py = b * (ay * bx - ax * by)
    # b = (ay * px - ax * py) / (ay * bx - ax * by)

    bn = ay * px - ax * py
    bd = ay * bx - ax * by
    if bn % bd != 0:
        continue
    b = bn // bd

    an = px - b * bx
    ad = ax
    if an % ad != 0:
        continue
    a = an // ad

    ans += a * 3 + b
print(ans)
