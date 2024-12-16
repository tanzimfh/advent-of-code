import re

with open("input.txt") as f:
    inp = f.read()

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

ans = 0
for match in pattern.finditer(inp):
    ans += int(match.group(1)) * int(match.group(2))
print(ans)