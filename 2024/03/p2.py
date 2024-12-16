import re

with open("input.txt") as f:
    inp = f.read()

mul_str = r"mul\((\d{1,3}),(\d{1,3})\)"
do_str = r"do\(\)"
dont_str = r"don't\(\)"

pattern = re.compile(f"{mul_str}|{do_str}|{dont_str}")

ans = 0
enabled = True
for match in pattern.finditer(inp):
    if match.group() == "do()":
        enabled = True
    elif match.group() == "don't()":
        enabled = False
    elif enabled:
        ans += int(match.group(1)) * int(match.group(2))
print(ans)
