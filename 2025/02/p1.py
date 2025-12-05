from elf import get_puzzle_input, submit_puzzle_answer

input_text = get_puzzle_input(2025, 2)

id_ranges = input_text.split(",")
ans = 0
for id_range in id_ranges:
    start, end = map(int, id_range.split("-"))
    for id in range(start, end + 1):
        str_id = str(id)
        mid_index = len(str_id) // 2
        if str_id[:mid_index] == str_id[mid_index:]:
            ans += id

print(submit_puzzle_answer(2025, 2, 1, ans))
