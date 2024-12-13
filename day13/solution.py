import sys
import re
from sympy import Matrix, solve_linear_system
from sympy.abc import x, y

class Machine:

    def __init__(
        self,
        ax: int,
        ay: int,
        bx: int,
        by: int,
        px: int,
        py: int
    ):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.px = px
        self.py = py
        pass

    def __repr__(self) -> str:
        return f"Machine (Button A: X+{self.ax}, Y+{self.ay}; Button B: X+{self.bx}, Y+{self.by}; Prize: X={self.px}, Y={self.py})"

def part1(input_list: list[str]) -> int:
    machines: list[Machine] = []

    i = 0
    while i < len(input_list):
        temp_data = []
        for j in range(i, i + 3):
            regex = re.compile(r"(\d+).+(?:\+|\=)(\d+)")
            matches = [x for xs in regex.findall(input_list[j]) for x in xs]
            temp_data.extend([int(x) for x in matches])
        machines.append(Machine(*temp_data))
        i += 4
    
    total = 0
    for machine in machines:
        cost = solve(machine)
        total += cost                                 
    return total

def solve(machine: Machine):
    system = Matrix(((machine.ax, machine.bx, machine.px), (machine.ay, machine.by, machine.py)))
    result = solve_linear_system(system, x, y)
    if result is None:
        return 0
    if result[x].is_integer and result[y].is_integer:
        return result[x]*3+result[y]
    return 0

def part2(input_list: list[str]) -> int:
    machines: list[Machine] = []

    i = 0
    while i < len(input_list):
        temp_data = []
        for j in range(i, i + 3):
            regex = re.compile(r"(\d+).+(?:\+|\=)(\d+)")
            matches = [x for xs in regex.findall(input_list[j]) for x in xs]
            temp_data.extend([int(x) for x in matches])
        temp_data[4] += 10000000000000
        temp_data[5] += 10000000000000
        machines.append(Machine(*temp_data))
        i += 4
    
    total = 0
    for machine in machines:
        total += solve(machine)               
    return total

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
        print(
        f"Part 1 answer: {part1(lines)} Part 2 answer: {part2(lines)}")
