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
        self.ram = [0] * 256
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

    def ram_read(self, mar):
        if mar <= len(self.ram) - 1:
            return self.ram[mar]
        return 0

    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == ADD:
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        elif op == MUL:
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def handle_ldi(self, op_a, op_b):
        self.reg[op_a] = op_b

    def handle_prn(self, op_a, _op_b):
        print(self.reg[op_a])

    def handle_hlt(self, _op_a, _op_b):
        self.running = False

    def run(self):
        """Run the CPU."""
        while self.running:
        # set memory at pc counter to intruction register
            self.ir = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            # self.branch_table[self.ir](operand_a, operand_b)
            self.branch_table(operand_a, operand_b)

            self.pc += 1 + (self.ir >> 6)