with open("input.txt") as f:
    stones = list(map(int, f.readline().split()))

for blink in range(25):
    inserts = {}
    for i, s in enumerate(stones):
        str_s = str(s)
        if s == 0:
            stones[i] = 1
        elif len(str_s) % 2 == 0:
            stones[i] = int(str_s[: len(str_s) // 2])
            inserts[i + 1 + len(inserts)] = int(str_s[len(str_s) // 2 :])
        else:
            stones[i] *= 2024

    new_stones = [0] * (len(stones) + len(inserts))
    stones_i = 0
    for i in range(len(new_stones)):
        if i in inserts:
            new_stones[i] = inserts[i]
        else:
            new_stones[i] = stones[stones_i]
            stones_i += 1
    stones = new_stones
print(len(stones))
