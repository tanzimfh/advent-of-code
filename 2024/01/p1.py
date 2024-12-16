left, right = [], []

with open("input.txt") as f:
    for line in f:
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)

left.sort()
right.sort()

ans = 0
for i in range(len(left)):
    ans += abs(left[i] - right[i])
print(ans)
