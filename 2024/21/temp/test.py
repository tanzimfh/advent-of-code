class numpad_robot:
    def __init__(self):
        self.numpad = ["789", "456", "123", " 0A"]
        self.r = 3
        self.c = 2
        self.code = ""

    def move(self, dir):
        d = {
            "^": (-1, 0),
            "v": (1, 0),
            "<": (0, -1),
            ">": (0, 1),
        }
        if dir == "A":
            self.code += self.numpad[self.r][self.c]
        else:
            dr, dc = d[dir]
            self.r += dr
            if not 0 <= self.r <= 3:
                print("PANIC!")
                exit()
            self.c += dc
            if not 0 <= self.c <= 2:
                print("PANIC!")
                exit()
            if self.numpad[self.r][self.c] == " ":
                print("PANIC!")
                exit()


class dpad_robot:
    def __init__(self, next_robot):
        self.dpad = [" ^A", "<v>"]
        self.r = 0
        self.c = 2
        self.next_robot = next_robot

    def move(self, dir):
        d = {
            "^": (-1, 0),
            "v": (1, 0),
            "<": (0, -1),
            ">": (0, 1),
        }
        if dir == "A":
            self.next_robot.move(self.dpad[self.r][self.c])
        else:
            dr, dc = d[dir]
            self.r += dr
            if not 0 <= self.r <= 1:
                print("PANIC!")
                exit()
            self.c += dc
            if not 0 <= self.c <= 2:
                print("PANIC!")
                exit()
            if self.dpad[self.r][self.c] == " ":
                print("PANIC!")
                exit()


nr = numpad_robot()
dr = dpad_robot(nr)
human = dpad_robot(dr)

for move in "<<vAA>A^>AA<Av>A^AvA^A<<vA^>>AAvA^Av<A^>AA<A>Av<A<A^>>AAA<Av>A^A":
    human.move(move)
print(nr.code)
