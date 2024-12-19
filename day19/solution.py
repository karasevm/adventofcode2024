import sys
from functools import cache


@cache
def count_combos(colors: tuple[str], target: str, target_part: str):
    count = 0

    if target_part == target:
        return 1
    
    target_part_len = len(target_part)
    for color in colors:
        color_len = len(color)
        if (
            target_part_len + color_len <= len(target)
            and target[target_part_len : target_part_len + color_len] == color
        ):
            count += count_combos(colors, target, target_part + color)

    return count


def part1(input_list: list[str]) -> int:
    colors = input_list[0].split(", ")
    targets = input_list[2:]

    count = 0
    for target in targets:
        if count_combos(tuple(colors), target, "") > 0:
            count += 1
    return count


def part2(input_list: list[str]) -> int:
    colors = input_list[0].split(", ")
    targets = input_list[2:]

    count = 0
    for target in targets:
        count += count_combos(tuple(colors), target, "")
    return count


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
