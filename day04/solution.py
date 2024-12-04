import sys


def check_directions(row: int, col: int, grid: list[list[int]]) -> int:
    offsets = [
        [(0, 1), (0, 2), (0, 3)],
        [(1, 1), (2, 2), (3, 3)],
        [(1, 0), (2, 0), (3, 0)],
        [(1, -1), (2, -2), (3, -3)],
        [(-1, -1), (-2, -2), (-3, -3)],
        [(-1, 0), (-2, 0), (-3, 0)],
        [(0, -1), (0, -2), (0, -3)],
        [(-1, 1), (-2, 2), (-3, 3)],
    ]
    direction_count = 0

    for offset_direction in offsets:
        queue = ["M", "A", "S"]
        for offset_row, offset_col in offset_direction:
            try:
                letter = queue.pop(0)
                if row + offset_row < 0 or col + offset_col < 0:
                    raise
                if grid[row + offset_row][col + offset_col] == letter:
                    if letter == "S":
                        direction_count += 1
                    continue
                break
            except:
                break
    return direction_count


def part1(input_list: list[str]) -> int:
    grid = []
    for line in input_list:
        grid.append(list(line))

    xmas_count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "X":
                xmas_count += check_directions(y, x, grid)
    return xmas_count


def check_x_mas(row: int, col: int, grid: list[list[str]]) -> bool:
    offsets_ne = [(-1, 1), (1, -1)]
    offsets_nw = [(1, 1), (-1, -1)]

    queue_ne = ["M", "S"]
    queue_nw = ["M", "S"]
    for offset_ne_row, offset_ne_col in offsets_ne:

        if row + offset_ne_row < 0 or col + offset_ne_col < 0:
            break
        try:
            queue_ne.remove(grid[row + offset_ne_row][col + offset_ne_col])
        except:
            break

    for offset_nw_row, offset_nw_col in offsets_nw:

        if row + offset_nw_row < 0 or col + offset_nw_col < 0:
            break
        try:
            queue_nw.remove(grid[row + offset_nw_row][col + offset_nw_col])
        except:
            break

    if (len(queue_ne) + len(queue_nw)) == 0:
        return True
    return False


def part2(input_list: list[str]) -> int:
    grid = []
    for line in input_list:
        grid.append(list(line))

    xmas_count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "A":
                xmas_count += check_x_mas(y, x, grid)
    return xmas_count


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
