class CPU:
    def __init__(self):
        self.pc = 1
        self.ir = 0
        self.memory = [0] * 256
        self.reg = [0] * 8

        self.reg[7] = 0xf4
        self.sp = self.reg[7]

