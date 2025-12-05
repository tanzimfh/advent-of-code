from elf import get_puzzle_input, submit_puzzle_answer

input_text = get_puzzle_input(2025, 4)
grid = input_text.splitlines()

ans = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] != "@":
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
            ans += 1

print(submit_puzzle_answer(2025, 4, 1, ans))
