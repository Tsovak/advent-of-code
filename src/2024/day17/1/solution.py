import os


def read_input() -> list[str]:
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data.txt')
    with open(filename, "rb") as f:
        return [line.decode("utf-8").strip() for line in f.readlines()]


class ThreeBitComputer:
    def __init__(self, program, register_a=0, register_b=0, register_c=0):
        self.program = program
        self.registers = {
            'A': register_a,
            'B': register_b,
            'C': register_c
        }
        self.instruction_pointer = 0
        self.output = []

    def get_operand_value(self, operand_type, operand):
        if operand_type == 'literal':
            return operand

        # combo operands
        combo_map = {
            0: 0, 1: 1, 2: 2, 3: 3,
            4: self.registers['A'],
            5: self.registers['B'],
            6: self.registers['C']
        }
        return combo_map[operand]

    def run(self):
        while self.instruction_pointer < len(self.program):
            opcode = self.program[self.instruction_pointer]

            # stop if we're at the end of the program
            if self.instruction_pointer + 1 >= len(self.program):
                break

            operand = self.program[self.instruction_pointer + 1]

            if opcode == 0:  # adv
                operand_value = self.get_operand_value('combo', operand)
                self.registers['A'] //= 2 ** operand_value

            elif opcode == 1:  # bxl
                operand_value = self.get_operand_value('literal', operand)
                self.registers['B'] ^= operand_value

            elif opcode == 2:  # bst
                operand_value = self.get_operand_value('combo', operand)
                self.registers['B'] = operand_value % 8

            elif opcode == 3:  # jnz
                operand_value = self.get_operand_value('literal', operand)
                if self.registers['A'] != 0:
                    self.instruction_pointer = operand_value
                    continue  # skip standard pointer increment

            elif opcode == 4:  # bxc
                self.registers['B'] ^= self.registers['C']

            elif opcode == 5:  # out
                operand_value = self.get_operand_value('combo', operand)
                self.output.append(operand_value % 8)

            elif opcode == 6:  # bdv
                operand_value = self.get_operand_value('combo', operand)
                self.registers['B'] = self.registers['A'] // (2 ** operand_value)

            elif opcode == 7:  # cdv
                operand_value = self.get_operand_value('combo', operand)
                self.registers['C'] = self.registers['A'] // (2 ** operand_value)

            self.instruction_pointer += 2

        return ','.join(str(x) for x in self.output)


lines = read_input()
registers = {}
for line in lines:
    if line.startswith('Register'):
        reg, value = line.strip().split(': ')
        registers[reg.split()[1]] = int(value)
    elif line.startswith('Program:'):
        program = list(map(int, line.split(': ')[1].split(',')))

comp = ThreeBitComputer(
    program,
    register_a=registers.get('A', 0),
    register_b=registers.get('B', 0),
    register_c=registers.get('C', 0)
)

result = comp.run()
print(result)
