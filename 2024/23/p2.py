with open("input.txt") as f:
    connections = [line.strip().split("-") for line in f]


def to_int(s):
    return (ord(s[0]) - ord("a")) * 26 + (ord(s[1]) - ord("a"))


def to_str(i):
    return chr((i // 26) + ord("a")) + chr((i % 26) + ord("a"))


n = 26**2
adj_list = [set() for _ in range(n)]
for a, b in connections:
    a, b = to_int(a), to_int(b)
    adj_list[a].add(b)
    adj_list[b].add(a)


def dfs(computer):
    global ans
    if computer in visited or tuple(sorted(list(visited) + [computer])) in seen:
        return
    for v in visited:
        if computer not in adj_list[v]:
            return
    visited.add(computer)
    seen.add(tuple(sorted(visited)))
    if len(visited) > len(ans):
        ans = visited.copy()
    for v in adj_list[computer]:
        dfs(v)
    visited.remove(computer)


ans = set()
visited = set()
seen = set()
for i in range(n):
    dfs(i)
print(",".join(sorted([to_str(i) for i in ans])))
