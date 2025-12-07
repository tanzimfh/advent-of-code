from elf import get_puzzle_input, submit_puzzle_answer

input_text = get_puzzle_input(2025, 7)
grid = [list(line) for line in input_text.splitlines()]
m, n = len(grid), len(grid[0])
# number of paths the beam can take to reach each cell
weight_grid = [[0 for _ in range(n)] for _ in range(m)]

s_index = grid[0].index("S")
weight_grid[1][s_index] = 1  # initial beam has only one path from S

ans = 0
for row in range(2, m):
    for col in range(n):
        above = weight_grid[row - 1][col]  # number of paths to cell above
        if above > 0:
            if grid[row][col] == "^":
                # same number of paths on each side of splitter
                # in addition to any other paths to those cells
                if 0 < col:
                    weight_grid[row][col - 1] += above
                if col < n - 1:
                    weight_grid[row][col + 1] = above
            else:
                weight_grid[row][col] += above
ans = sum(weight_grid[-1])  # number of paths to end

print(submit_puzzle_answer(2025, 7, 2, ans))
