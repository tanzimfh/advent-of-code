from collections import defaultdict

prereqs = defaultdict(set)
orders = []

with open("input.txt") as f:
    for line in f:
        if "|" in line:
            prereq, page = map(int, line.split("|"))
            prereqs[page].add(prereq)
        elif "," in line:
            orders.append(list(map(int, line.split(","))))

ans = 0
for order in orders:
    unallowed = set()
    for page in order:
        if page in unallowed:
            break
        unallowed.update(prereqs[page])
    else:
        ans += order[len(order) // 2]
print(ans)
