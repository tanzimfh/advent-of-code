with open("input.txt") as file:
    for line in file:
        if line.startswith("Register A"):
            A = int(line.split()[-1])
        elif line.startswith("Program"):
            program = list(map(int, line.split()[-1].split(",")))


def run(A, B=0, C=0):
    def combo(x):
        if 0 <= x <= 3:
            return x
        return {4: A, 5: B, 6: C}[x]

    out = []
    ip = 0
    while 0 <= ip < len(program):
        opcode, operand = program[ip], program[ip + 1]
        if opcode == 0:
            A = int(A / 2 ** combo(operand))
        elif opcode == 1:
            B ^= operand
        elif opcode == 2:
            B = combo(operand) % 8
        elif opcode == 3:
            if A != 0:
                ip = operand
                continue
        elif opcode == 4:
            B ^= C
        elif opcode == 5:
            out.append(combo(operand) % 8)
        elif opcode == 6:
            B = int(A / 2 ** combo(operand))
        elif opcode == 7:
            C = int(A / 2 ** combo(operand))
        ip += 2
    return out


def dfs(i, A):
    if i == -1:
        return A

    A *= 8
    for A in range(A, A + 8):
        if run(A) == program[i:]:
            ans = dfs(i - 1, A)
            if ans != -1:
                return ans
    return -1


print(dfs(len(program) - 1, 0))
