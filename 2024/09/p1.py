with open("input.txt") as f:
    disk_map = f.read().strip()

arr = []
freq = {}
empty = False
id = 0
i = 0
for c in disk_map:
    c = int(c)
    if empty:
        arr += ["."] * c
    else:
        arr += [str(id)] * c
        freq[id] = c
        id += 1
    i += c
    empty = not empty

i, j = 0, len(arr) - 1
while True:
    while arr[i] != ".":
        i += 1
    while arr[j] == ".":
        j -= 1
    if i >= j:
        break
    arr[i] = arr[j]
    arr[j] = "."
    i += 1
    j -= 1

ans = 0
for i in range(len(arr)):
    if arr[i] != ".":
        ans += i * int(arr[i])
print(ans)
