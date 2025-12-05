from elf import get_puzzle_input, submit_puzzle_answer

input_text = get_puzzle_input(2025, 4)
grid = [list(line) for line in input_text.splitlines()]

ans = 0
while True:
    curr_ans = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] not in {"@", "x"}:
                continue

            count_adj = -1  # will count self
            for ar in range(r - 1, r + 2):
                for ac in range(c - 1, c + 2):
                    if (
                        0 <= ar < len(grid)
                        and 0 <= ac < len(grid[0])
                        and grid[ar][ac] == "@"
                    ):
                        count_adj += 1
            if count_adj < 4:
                curr_ans += 1
                grid[r][c] = "x"
    ans += curr_ans

    if curr_ans == 0:
        break
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == "x":
                grid[r][c] = "."

print(submit_puzzle_answer(2025, 4, 2, ans))
