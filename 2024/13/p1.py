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
    for a in range(101):
        for b in range(101):
            if (a * ax + b * bx, a * ay + b * by) == (px, py):
                ans += a * 3 + b
print(ans)
