from elf import get_puzzle_input, submit_puzzle_answer
from math import prod

input_text = get_puzzle_input(2025, 6)
input_text = input_text.splitlines()

ans = 0
nums = []
for col in range(len(input_text[0]) - 1, -1, -1):
    num = ""
    for row in range(len(input_text) - 1):
        c = input_text[row][col]
        if c != " ":
            num += c
    if num:
        nums.append(int(num))

    op = input_text[-1][col]
    if op != " ":
        func = sum if op == "+" else prod
        ans += func(nums)
        nums = []

print(submit_puzzle_answer(2025, 6, 2, ans))
