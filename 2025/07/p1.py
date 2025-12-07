from elf import get_puzzle_input, submit_puzzle_answer

input_text = get_puzzle_input(2025, 7)
grid = [list(line) for line in input_text.splitlines()]
m, n = len(grid), len(grid[0])

s_index = grid[0].index("S")
grid[1][s_index] = "|"  # start off the initial beam

ans = 0
for row in range(2, m):
    for col in range(n):
        if grid[row - 1][col] == "|":  # beam directly above
            if grid[row][col] == "^":  # splitter
                ans += 1
                if 0 < col:
                    grid[row][col - 1] = "|"
                if col < n - 1:
                    grid[row][col + 1] = "|"
            else:  # no splitter, continue beam from above
                grid[row][col] = "|"

print(submit_puzzle_answer(2025, 7, 1, ans))
