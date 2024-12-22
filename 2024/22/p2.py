with open("input.txt") as f:
    initials = [int(line) for line in f]


def get_next(secret):
    def mix(a, b):
        return a ^ b

    def prune(a):
        return a % 16777216

    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret


seq_prices = {}
for i, secret in enumerate(initials):
    seen = set()
    seq = []
    for i in range(2000):
        next_secret = get_next(secret)
        seq.append(next_secret % 10 - secret % 10)
        if len(seq) == 5:
            seq.pop(0)
            tup = tuple(seq)
            if tup not in seen:
                seq_prices[tup] = seq_prices.get(tup, 0) + next_secret % 10
                seen.add(tup)
        secret = next_secret
print(max(seq_prices.values()))
