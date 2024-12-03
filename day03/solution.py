import sys
import re

def part1(input_list: list[str]) -> int:
    result = 0
    for line in input_list:
        regex = re.compile(r"(mul\((\d{1,3})\,(\d{1,3})\))")
        matches = regex.findall(line)
        for match in matches:
            result += int(match[1]) * int(match[2])
    return result

def part2(input_list: list[str]) -> int:
    result = 0
    include = True
    for line in input_list:
        regex = re.compile(r"(mul\((\d{1,3})\,(\d{1,3})\)|do\(\)|don't\(\))")
        matches = regex.findall(line)
        for match in matches:
            if match[0] == "don't()":
                include = False
            elif match[0] == "do()":
                include = True
            elif include:
                result += int(match[1]) * int(match[2])
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
        print(
        f"Part 1 answer: {part1(lines)} Part 2 answer: {part2(lines)}")
