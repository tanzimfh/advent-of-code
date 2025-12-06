from elf import get_puzzle_input, submit_puzzle_answer
from math import prod

input_text = get_puzzle_input(2025, 6)
grid = [line.split() for line in input_text.splitlines()]

ans = 0
for col, op in enumerate(grid[-1]):
    func = sum if op == "+" else prod
    ans += func(int(grid[row][col]) for row in range(len(grid) - 1))

print(submit_puzzle_answer(2025, 6, 1, ans))
