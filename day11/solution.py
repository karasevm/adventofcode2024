import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def get_new_number(number: int, depth: int, target_depth: int) -> int:
    stringed_number = str(number)
    number_len = len(stringed_number)
    if depth == target_depth:
        return 1
    if number == 0:
        return get_new_number(1, depth + 1, target_depth)
    elif number_len % 2 == 0:
        return get_new_number(int(stringed_number[:number_len//2]), depth + 1, target_depth) + get_new_number(int(stringed_number[number_len//2:]), depth + 1, target_depth)
    else:
        return get_new_number(number*2024, depth + 1, target_depth)

def part1(input_list: list[str]) -> int:
    numbers = list([*map(int, input_list[0].split(" "))])

    result = 0
    for number in numbers:
        result+= get_new_number(number, 0, 25)
        
    return result

def part2(input_list: list[str]) -> int:
    numbers = list([*map(int, input_list[0].split(" "))])

    result = 0
    for number in numbers:
        result+= get_new_number(number, 0, 75)
        
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
