designs = []
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if "," in line:
            towels = line.split(", ")
        elif line != "":
            designs.append(line)


def possible(design, i=0):
    if i == len(design):
        return 1

    if i in dp[design]:
        return dp[design][i]

    dp[design][i] = 0
    for towel in towels:
        if design[i:].startswith(towel):
            dp[design][i] += possible(design, i + len(towel))
    return dp[design][i]


dp = {d: {} for d in designs}

print(sum(possible(d) for d in designs))
