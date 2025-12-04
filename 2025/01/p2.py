from elf import get_puzzle_input, submit_puzzle_answer

input_text = get_puzzle_input(2025, 1)

ans = 0
dial_position = 50
for line in input_text.splitlines():
    direction = 1 if line[0] == "R" else -1
    distance = int(line[1:])

    before_mod = dial_position + direction * distance
    ans += abs(before_mod // 100)
    # if we were on 0, wrapping left should not increment ans again
    ans -= (before_mod < 0) and (dial_position == 0)

    dial_position = before_mod % 100
    # count landing on 0 when rotating left
    ans += (dial_position == 0) and (direction == -1)

print(submit_puzzle_answer(2025, 1, 2, ans))
