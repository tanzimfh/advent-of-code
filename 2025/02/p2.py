from elf import get_puzzle_input, submit_puzzle_answer

input_text = get_puzzle_input(2025, 2)


def repeated(str_id: str, seq_len: int) -> bool:
    initial_seq = str_id[:seq_len]
    for i in range(seq_len, len(str_id), seq_len):
        if str_id[i : i + seq_len] != initial_seq:
            return False
    return True


id_ranges = input_text.split(",")
ans = 0
for id_range in id_ranges:
    start, end = map(int, id_range.split("-"))
    for id in range(start, end + 1):
        str_id = str(id)
        mid_index = len(str_id) // 2
        for seq_len in range(1, mid_index + 1):
            if repeated(str_id, seq_len):
                ans += id
                break

print(submit_puzzle_answer(2025, 2, 2, ans))
