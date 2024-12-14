import sys
import re
import math


class Robot:

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def simulate_one_second(self, x_boundary, y_boundary):
        self.x = (self.x + self.vx) % x_boundary
        self.y = (self.y + self.vy) % y_boundary

    def __repr__(self):
        return f"Robot (x = {self.x}, y = {self.y}, vx = {self.vx}, vy = {self.vy})"

    def copy(self):
        return Robot(self.x, self.y, self.vx, self.vy)


def solve_robot(robot: Robot, iters=100, x_boundary=11, y_boundary=7):

    states = set()
    loop_len = 0
    working_robot = robot.copy()
    while (working_robot.x, working_robot.y) not in states:
        states.add((working_robot.x, working_robot.y))
        working_robot.simulate_one_second(x_boundary, y_boundary)
        loop_len += 1
    for _ in range(iters % loop_len):
        working_robot.simulate_one_second(x_boundary, y_boundary)

    return working_robot, loop_len


def part1(input_list: list[str]) -> int:
    robots = []
    regex = re.compile(r"p=(\d+)\,(\d+) v=(-?\d+)\,(-?\d+)")
    for line in input_list:
        matches = regex.findall(line)
        robots.append(Robot(*([int(x) for x in matches[0]])))

    x_boundary = 101
    y_boundary = 103

    counts = [0, 0, 0, 0]
    new_robots = []
    for robot in robots:
        new_robot, _ = solve_robot(robot, 100, x_boundary, y_boundary)
        new_robots.append(new_robot)
        if new_robot.x < x_boundary // 2 and new_robot.y < y_boundary // 2:
            counts[0] += 1
        elif new_robot.x > (x_boundary) // 2 and new_robot.y < y_boundary // 2:
            counts[1] += 1
        elif new_robot.x > (x_boundary) // 2 and new_robot.y > (y_boundary) // 2:
            counts[2] += 1
        elif new_robot.x < x_boundary // 2 and new_robot.y > (y_boundary) // 2:
            counts[3] += 1
    result = counts[0]
    for n in counts[1:]:
        result *= n

    return result


def print_robots(robots: list[Robot], x_boundary, y_boundary, count) -> None:
    coords = set()
    for robot in robots:
        coords.add((robot.x, robot.y))
    with open("output.txt", "a") as myfile:
        myfile.write(f"#############{count}###############\n")
        for row in range(y_boundary):
            for col in range(x_boundary):
                if (col, row) in coords:
                    myfile.write("#")
                else:
                    myfile.write(".")
            myfile.write("\n")


def count_consecutive(robots: list[Robot], x_boundary, y_boundary, count) -> int:
    max_consecutive = 0
    coords = set()
    for robot in robots:
        coords.add((robot.x, robot.y))
    for row in range(y_boundary):
        curr_max_consecutive = 0
        for col in range(x_boundary):
            if (col, row) in coords:
                curr_max_consecutive += 1
        if curr_max_consecutive > max_consecutive:
            max_consecutive = curr_max_consecutive
    return max_consecutive


def part2(input_list: list[str]) -> int:
    robots: list[Robot] = []
    regex = re.compile(r"p=(\d+)\,(\d+) v=(-?\d+)\,(-?\d+)")
    for line in input_list:
        matches = regex.findall(line)
        robots.append(Robot(*([int(x) for x in matches[0]])))

    x_boundary = 101
    y_boundary = 103

    loop_lens = []
    count = 0

    for robot in robots:
        _, loop_len = solve_robot(robot, 100, x_boundary, y_boundary)
        loop_lens.append(loop_len)

    lcm = math.lcm(*loop_lens)

    consecutive_max = 0
    consecutive_max_count = 0
    while count <= lcm:
        count += 1
        for robot in robots:
            robot.simulate_one_second(x_boundary, y_boundary)

        # print_robots(robots, x_boundary, y_boundary, count)
        consecutive = count_consecutive(robots, x_boundary, y_boundary, count)
        if consecutive > consecutive_max:
            consecutive_max = consecutive
            consecutive_max_count = count

    return consecutive_max_count


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
