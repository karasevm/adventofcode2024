import sys


def use_combo_operand(operand: int, register_a, register_b, register_c):
    if operand < 4:
        return operand
    elif operand == 4:
        return register_a
    elif operand == 5:
        return register_b
    elif operand == 6:
        return register_c
    raise ValueError("Unexpected operand")


def simulate_state(register_a, register_b, register_c, program) -> list[int]:
    output_buffer = []
    cycles = 0
    pc = 0
    while pc < len(program) - 1:
        opcode = program[pc]
        cycles += 1
        match opcode:
            case 0:  # adv
                register_a = int(register_a / 2 ** use_combo_operand(program[pc + 1], register_a, register_b, register_c))
                pc += 2
            case 1:  # bxl
                register_b ^= program[pc + 1]
                pc += 2
            case 2:  # bst
                register_b = (use_combo_operand(program[pc + 1], register_a, register_b, register_c) % 8)
                pc += 2
            case 3:  # jnz
                if register_a != 0:
                    pc = program[pc + 1]
                else:
                    pc += 2
            case 4:  # bxc
                register_b ^= register_c
                pc += 2
            case 5:  # out
                output_buffer.append(use_combo_operand(program[pc + 1], register_a, register_b, register_c) % 8)
                pc += 2
            case 6:  # bdv
                register_b = int(register_a / 2 ** use_combo_operand(program[pc + 1], register_a, register_b, register_c))
                pc += 2
            case 7:  # cdv
                register_c = int(register_a / 2 ** use_combo_operand(program[pc + 1], register_a, register_b, register_c))
                pc += 2
    return output_buffer


def part1(input_list: list[str]) -> str:
    register_a = int(input_list[0].split(": ")[1])
    register_b = int(input_list[1].split(": ")[1])
    register_c = int(input_list[2].split(": ")[1])

    program = [int(x) for x in input_list[4].split(": ")[1].split(",")]
    output = simulate_state(register_a, register_b, register_c, program)
    return ",".join([str(x) for x in output])


def part2(input_list: list[str]) -> int:
    register_a = int(input_list[0].split(": ")[1])
    register_b = int(input_list[1].split(": ")[1])
    register_c = int(input_list[2].split(": ")[1])
    program = [int(x) for x in input_list[4].split(": ")[1].split(",")]

    result = 0
    target_count = len(program) - 1
    while target_count >= 0:
        while True:
            if simulate_state(result, register_b, register_c, program) == program[target_count:]:
                result *= 8
                break
            result += 1
        target_count -= 1
    result //= 8
    return result


if __name__ == "__main__":
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        print("Error opening the file, try again")
        sys.exit(1)
    with f:
        lines = f.readlines()
        f.close()
        lines = [line.rstrip() for line in lines]
        print(f"Part 1 answer: {part1(lines)} Part 2 answer: {part2(lines)}")
