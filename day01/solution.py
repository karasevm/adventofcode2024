import sys


def part1(input_list: list[str]) -> int:
    left = []
    right = []
    for line in input_list:
        nums = line.split("   ")
        left.append(int(nums[0]))
        right.append(int(nums[1]))
    left.sort()
    right.sort()
    answer = 0
    for i in range(len(left)):
        answer += abs(left[i] - right[i])
    return answer

def part2(input_list: list[str]) -> int:
    left = []
    right = []
    for line in input_list:
        nums = line.split("   ")
        left.append(int(nums[0]))
        right.append(int(nums[1]))
    answer = 0
    for i in range(len(left)):
        print(left[i], right.count(left[i]))
        answer += left[i] * right.count(left[i])
    return answer

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
