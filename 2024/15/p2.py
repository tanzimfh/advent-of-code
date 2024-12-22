grid = []
moves = ""
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if "<" in line:
            moves += line
            continue
        line = (
            line.replace("#", "##")
            .replace("O", "[]")
            .replace(".", "..")
            .replace("@", "@.")
        )
        if "@" in line:
            pr, pc = (len(grid), line.index("@"))
        grid.append(list(line))


def can_move(r, c, dr):
    if grid[r][c] in "#.":
        return grid[r][c] == "."
    return can_move(r + dr, c, dr) and can_move(
        r + dr, c + (1 if grid[r][c] == "[" else -1), dr
    )


def make_move(r, left, dr):
    if grid[r + dr][left : left + 2] == [".", "."]:
        grid[r + dr][left : left + 2] = ["[", "]"]
        grid[r][left : left + 2] = [".", "."]
        return

    flag = False
    if grid[r + dr][left - 1] == "[":
        make_move(r + dr, left - 1, dr)
        flag = True
    if grid[r + dr][left + 2] == "]":
        make_move(r + dr, left + 1, dr)
        flag = True

    if not flag:
        make_move(r + dr, left, dr)

    grid[r + dr][left : left + 2] = ["[", "]"]
    grid[r][left : left + 2] = [".", "."]


direction = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

for i, move in enumerate(moves):
    dr, dc = direction[move]
    tr, tc = pr + dr, pc + dc

    if move in "<>":
        while grid[tr][tc] != "#":
            if grid[tr][tc] == ".":
                break
            tc += dc
        else:
            continue
        grid[tr][tc] = "]" if move == "<" else "["  # to be flipped
        grid[pr][pc] = "."
        while tc != pc:
            grid[tr][tc] = "[" if grid[tr][tc] == "]" else "]"
            tc -= dc

        pc += dc
        grid[pr][pc] = "@"

    elif (
        grid[pr + dr][pc] in "[]"
        and can_move(pr + dr, pc, dr)
        and can_move(pr + dr, pc + (1 if grid[pr + dr][pc] == "[" else -1), dr)
    ):
        left = pc
        if grid[pr + dr][pc] == "]":
            left -= 1

        make_move(pr + dr, left, dr)
        grid[pr][pc] = "."
        pr += dr
        grid[pr][left : left + 2] = ["@", "."] if left == pc else [".", "@"]

    elif grid[pr + dr][pc] == ".":
        grid[pr][pc] = "."
        pr += dr
        grid[pr][pc] = "@"

ans = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "[":
            ans += 100 * r + c
print(ans)
