from elf import get_puzzle_input, submit_puzzle_answer

input_text = get_puzzle_input(2025, 1)

ans = 0
dial_position = 50
for line in input_text.splitlines():
    direction = 1 if line[0] == "R" else -1
    distance = int(line[1:])

    dial_position = (dial_position + direction * distance) % 100
    ans += dial_position == 0

print(submit_puzzle_answer(2025, 1, 1, ans))
