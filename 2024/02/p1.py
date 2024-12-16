def safe(levels):
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    if not all(d > 0 for d in diffs) and not all(d < 0 for d in diffs):
        return False
    return all(1 <= abs(d) <= 3 for d in diffs)


ans = 0
with open("input.txt") as f:
    for line in f:
        if safe(list(map(int, line.split()))):
            ans += 1
print(ans)
