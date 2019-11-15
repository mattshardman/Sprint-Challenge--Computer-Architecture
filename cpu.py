import sys

LDI = 0b10000010
PRN = 0b01000111 
MUL = 0b10100010
ADD = 0b10100000
HLT = 0b00000001 
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
RTN = 0b00010001
CMP = 0b10100111
JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110
AND = 0b10101000
OR = 0b10101010
XOR = 0b10101011
NOT = 0b01101001
SHL = 0b10101100
SHR = 0b10101101
MOD = 0b10100010

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

    def branch_table(self, op_1, op_2):
        if op_1 and 0b1 << 5:
            self.alu(self.ir, op_1, op_2)

        else:
            branches = {
                LDI: self.handle_ldi,
                PRN: self.handle_prn,
                HLT: self.handle_hlt,
                PUSH: self.push,
                POP: self.pop,
                CALL: self.call,
                RTN: self.rtn,
            }

            branches[self.ir](op_1, op_2)

