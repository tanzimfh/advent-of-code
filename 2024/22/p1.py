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


ans = 0
for secret in initials:
    for i in range(2000):
        secret = get_next(secret)
    ans += secret
print(ans)
