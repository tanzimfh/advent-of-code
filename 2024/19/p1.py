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
        return True

    if i in dp[design]:
        return dp[design][i]

    for towel in towels:
        if design[i:].startswith(towel) and possible(design, i + len(towel)):
            dp[design][i] = True
            return True
    dp[design][i] = False
    return False


dp = {d: {} for d in designs}

print(sum(possible(d) for d in designs))
