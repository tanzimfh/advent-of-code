from elf import get_puzzle_input, submit_puzzle_answer

input_text = get_puzzle_input(2025, 3)

ans = 0
for line in input_text.splitlines():
    all_batteries = [int(c) for c in line]

    joltage = ""
    b_idx = -1
    for bn in range(12):
        start_idx = b_idx + 1
        possibilities = all_batteries[start_idx : len(all_batteries) - 11 + bn]
        b_idx = start_idx + possibilities.index(max(possibilities))
        b = all_batteries[b_idx]
        joltage += str(b)

    ans += int(joltage)

print(submit_puzzle_answer(2025, 3, 2, ans))
