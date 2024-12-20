with open("input.txt") as f:
    stones = list(map(int, f.readline().split()))


def process(s, blinks_left):
    if blinks_left == 0:
        return 1
    if (s, blinks_left) not in cache:
        str_s = str(s)
        if s == 0:
            cache[(s, blinks_left)] = process(1, blinks_left - 1)
        elif len(str_s) % 2 == 0:
            cache[(s, blinks_left)] = process(
                int(str_s[: len(str_s) // 2]), blinks_left - 1
            ) + process(int(str_s[len(str_s) // 2 :]), blinks_left - 1)
        else:
            cache[(s, blinks_left)] = process(s * 2024, blinks_left - 1)
    return cache[(s, blinks_left)]


cache = {}

print(sum(process(int(s), 75) for s in stones))
