equations = []
with open("input.txt") as f:
    for line in f:
        target, nums = line.split(": ")
        equations.append((int(target), list(map(int, nums.split()))))


def find(target, nums, sofar=0, i=0):
    if i == len(nums):
        return sofar == target
    return find(target, nums, sofar + nums[i], i + 1) or find(
        target, nums, sofar * nums[i], i + 1
    )


ans = 0
for target, nums in equations:
    if find(target, nums):
        ans += target
print(ans)
