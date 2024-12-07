import sys


def check_nums(nums: list[int], required_sum: int):
    if len(nums) == 1:
        if nums[0] == required_sum:
            return True
        return False

    mult_op = [nums[0] * nums[1], *nums[2:]]
    sum_op = [nums[0] + nums[1], *nums[2:]]

    return check_nums(mult_op, required_sum) or check_nums(sum_op, required_sum)


def part1(input_list: list[str]) -> int:
    eqs = []
    for line in input_list:
        eq_sum = int(line.split(":")[0])
        eq_nms = list(map(int, line.split(": ")[1].split(" ")))
        eqs.append([eq_sum, *eq_nms])

    result = 0
    for item in eqs:
        if check_nums(item[1:], item[0]):
            result += item[0]

    return result


def check_nums2(nums: list[int], required_sum: int):
    if len(nums) == 1:
        if nums[0] == required_sum:
            return True
        return False

    mult_op = [nums[0] * nums[1], *nums[2:]]
    sum_op = [nums[0] + nums[1], *nums[2:]]
    concat_op = [int(str(nums[0]) + str(nums[1])), *nums[2:]]

    return (
        check_nums2(mult_op, required_sum)
        or check_nums2(sum_op, required_sum)
        or check_nums2(concat_op, required_sum)
    )


def part2(input_list: list[str]) -> int:
    equations = []
    for line in input_list:
        eq_sum = int(line.split(":")[0])
        eq_nms = list(map(int, line.split(": ")[1].split(" ")))
        equations.append([eq_sum, *eq_nms])

    result = 0
    for item in equations:
        if check_nums2(item[1:], item[0]):
            result += item[0]
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
