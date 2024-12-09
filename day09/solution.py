import sys


def part1(input_list: str) -> int:
    is_file = True
    count = 0
    disk_data = []
    for num in input_list:
        num = int(num)
        fill_data = count
        if not is_file:
            fill_data = "."
        if is_file:
            count += 1
        disk_data.extend([fill_data] * num)
        is_file = not is_file
    for i in range(len(disk_data) - 1, -1, -1):
        if disk_data[i] != ".":
            try:
                target_index = disk_data[:i].index(".")
                disk_data[i], disk_data[target_index] = (
                    disk_data[target_index],
                    disk_data[i],
                )
            except:
                pass
    result = 0
    for id, data in enumerate(disk_data):
        if data != ".":
            result += id * int(data)
    return result


def part2(input_list: str) -> int:
    is_file = True
    count = 0
    disk_data = []
    for num in input_list:
        num = int(num)
        fill_data = count
        if not is_file:
            fill_data = "."
        if is_file:
            count += 1
        disk_data.extend([fill_data] * num)
        is_file = not is_file

    start_index = len(disk_data) - 1
    end_index = len(disk_data) - 1
    curr_id = -1
    while True:
        if end_index == 0:
            break
        if disk_data[start_index] == ".":
            start_index -= 1
            continue
        curr_id = disk_data[start_index]
        if end_index > start_index:
            end_index = start_index
        while True:
            if disk_data[end_index - 1] == curr_id:
                end_index -= 1
            else:
                break
        start_index += 1

        gap_start = 0
        gap_end = 0
        while True:
            if disk_data[gap_start] != ".":
                gap_start += 1
                continue

            if gap_start >= end_index:
                break

            if gap_end < gap_start:
                gap_end = gap_start

            while True:
                if disk_data[gap_end + 1] == ".":
                    gap_end += 1
                else:
                    break

            if gap_end + 1 - gap_start < start_index - end_index:
                gap_start = gap_end + 1
            else:
                break
            if gap_start >= end_index:
                break

        gap_end += 1
        block_len = start_index - end_index
        if gap_end <= end_index and gap_end - gap_start >= start_index - end_index:
            disk_data = (
                disk_data[0:gap_start]
                + [curr_id] * (block_len)
                + disk_data[gap_start + block_len : end_index]
                + ["."] * (block_len)
                + disk_data[start_index:]
            )
        start_index = end_index - 1
    result = 0
    for id, data in enumerate(disk_data):
        if data != ".":
            result += id * int(data)
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
        print(f"Part 1 answer: {part1(lines[0])} Part 2 answer: {part2(lines[0])}")
