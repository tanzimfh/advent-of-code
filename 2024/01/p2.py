from collections import defaultdict

left = []
right_freq = defaultdict(int)

with open("input.txt") as f:
    for line in f:
        a, b = map(int, line.split())
        left.append(a)
        right_freq[b] += 1

ans = 0
for l in left:
    ans += l * right_freq[l]
print(ans)
