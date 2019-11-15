import sys

class CPU:
    def __init__(self):
        self.pc = 1
        self.ir = 0
        self.memory = [0] * 256
        self.reg = [0] * 8

        self.reg[7] = 0xf4
        self.sp = self.reg[7]

    def load(self):
        f = open(sys.argv[1], "r")
        address = 0
        for line in f:
            ln = ''
            for char in line:
                if char == '#':
                    break
                if char == '\n':
                    break
                ln += char
            if len(ln) > 0:
                self.ram[address] = int(ln, 2)
                address += 1
