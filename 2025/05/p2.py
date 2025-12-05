from elf import get_puzzle_input, submit_puzzle_answer

input_text = get_puzzle_input(2025, 5)

ranges = []
for line in input_text.splitlines():
    if line == "":
        break
    ranges.append(tuple(map(int, line.split("-"))))
ranges.sort()

ans = 0
max_counted = 0  # max ID counted so far
for a, b in ranges:
    if max_counted >= b:
        continue
    starting = max(a, max_counted + 1)
    ans += b - starting + 1
    max_counted = b

print(submit_puzzle_answer(2025, 5, 2, ans))
