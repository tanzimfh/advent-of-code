values = {}
inputs = {}
max_z = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if ": " in line:
            k, v = line.split(": ")
            values[k] = int(v)
        elif " -> " in line:
            v, k = line.split(" -> ")
            inputs[k] = v
            if k.startswith("z"):
                max_z = max(max_z, int(k[1:]))

def get_value(wire):
    if wire not in values:
        i1, op, i2 = inputs[wire].split()
        v1, v2 = get_value(i1), get_value(i2)
        if op == "AND":
            values[wire] = v1 & v2
        elif op == "OR":
            values[wire] = v1 | v2
        elif op == "XOR":
            values[wire] = v1 ^ v2
    return values[wire]

ans = 0
for i in range(max_z, -1, -1):
    ans = ans * 2 + get_value("z" + str(i).zfill(2))
print(ans)