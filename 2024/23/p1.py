with open("input.txt") as f:
    connections = [line.strip().split("-") for line in f]


def to_int(s):
    return (ord(s[0]) - ord("a")) * 26 + (ord(s[1]) - ord("a"))


n = 26**2
adj_list = [set() for _ in range(n)]
for a, b in connections:
    a, b = to_int(a), to_int(b)
    adj_list[a].add(b)
    adj_list[b].add(a)

combinations = set()
for i in range(26):
    c1 = (ord("t") - ord("a")) * 26 + i
    for c2 in adj_list[c1]:
        for c3 in adj_list[c2]:
            if c3 in adj_list[c1]:
                combinations.add(tuple(sorted([c1, c2, c3])))
print(len(combinations))
