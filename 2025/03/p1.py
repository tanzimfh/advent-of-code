from elf import get_puzzle_input, submit_puzzle_answer

input_text = get_puzzle_input(2025, 3)

ans = 0
for line in input_text.splitlines():
    all_batteries = [int(c) for c in line]

    b1_possibilities = all_batteries[:-1]
    b1_idx = b1_possibilities.index(max(b1_possibilities))
    b1 = b1_possibilities[b1_idx]

    b2_possibilities = all_batteries[b1_idx + 1 :]
    b2_idx = b2_possibilities.index(max(b2_possibilities))
    b2 = b2_possibilities[b2_idx]

    ans += int(str(b1) + str(b2))

print(submit_puzzle_answer(2025, 3, 1, ans))
