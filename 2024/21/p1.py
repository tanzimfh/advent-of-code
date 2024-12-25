codes = []
with open("input.txt") as f:
    for line in f:
        codes.append(line.strip())

numpad_grid = ["789", "456", "123", " 0A"]
numpad_loc = {numpad_grid[r][c]: (r, c) for r in range(4) for c in range(3)}

dpad_grid = [" ^A", "<v>"]
dpad_loc = {dpad_grid[r][c]: (r, c) for r in range(2) for c in range(3)}


def moves(dr, dc, left_blocked):
    ret = ""
    if dc < 0 and not left_blocked:
        ret += "<" * (-dc)
    ret += "v" * dr
    ret += "^" * (-dr)
    if dc > 0:
        ret += ">" * dc
    elif left_blocked:
        ret += "<" * (-dc)
    return ret


def numpad(code):
    ret = ""
    r, c = 3, 2
    for char in code:
        nr, nc = numpad_loc[char]
        ret += moves(nr - r, nc - c, r == 3 and nc == 0) + "A"
        r, c = nr, nc
    return ret


def directional(code):
    ret = ""
    r, c = 0, 2
    for char in code:
        nr, nc = dpad_loc[char]
        ret += moves(nr - r, nc - c, r == 0 and nc == 0) + "A"
        r, c = nr, nc
    return ret


ans = 0
for code in codes:
    ans += len(directional(directional(numpad(code)))) * int(code[:-1])
print(ans)
