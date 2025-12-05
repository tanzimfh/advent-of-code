from elf import get_puzzle_input, submit_puzzle_answer

input_text = get_puzzle_input(2025, 5)

ranges = []
seen_blank = False
ans = 0
for line in input_text.splitlines():
    if line == "":
        seen_blank = True
        continue
    if not seen_blank:
        ranges.append(tuple(map(int, line.split("-"))))
    else:
        id = int(line)
        for a, b in ranges:
            if a <= id <= b:
                ans += 1
                break

print(submit_puzzle_answer(2025, 5, 1, ans))
