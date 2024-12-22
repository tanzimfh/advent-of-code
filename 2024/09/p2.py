with open("input.txt") as f:
    disk_map = f.read().strip()

arr = []
freq = {}
first = {}
empty = False
id = 0
i = 0
for c in disk_map:
    c = int(c)
    if empty:
        arr += ["."] * c
    else:
        first[id] = i
        arr += [str(id)] * c
        freq[id] = c
        id += 1
    i += c
    empty = not empty


def insert(id):
    i = 0
    while i < len(arr):
        if arr[i] == ".":
            l = 0
            while arr[i + l] == ".":
                l += 1
            if l >= freq[id]:
                for j in range(first[id], first[id] + freq[id]):
                    arr[j] = "."
                for j in range(freq[id]):
                    arr[i + j] = str(id)
                return True
            else:
                i += l
        elif arr[i] == str(id):
            return False
        i += 1
    return False


for id in sorted(freq.keys(), reverse=True):
    insert(id)

ans = 0
for i in range(len(arr)):
    if arr[i] != ".":
        ans += i * int(arr[i])
print(ans)
