import sys


def part1(input_list: list[str]) -> int:
    grid_size = 71
    input_limit = 1024
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    for n, line in enumerate(input_list):
        if n == input_limit:
            break
        x, y = [int(x) for x in line.split(",")]
        grid[y][x] = "#"

    offsets = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    queue = [(0, 0, 0)]
    visited = set()
    while len(queue) != 0:
        curr_row, curr_col, steps = queue.pop(0)
        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))
        if curr_row == len(grid) - 1 and curr_col == len(grid[0]) - 1:
            return steps
        for offset_row, offset_col in offsets:
            new_row = curr_row + offset_row
            new_col = curr_col + offset_col
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] != "#":
                    queue.append((new_row, new_col, steps + 1))
    return 0


def exit_exists(grid) -> bool:
    offsets = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    queue = [(0, 0, 0)]
    visited = set()
    while len(queue) != 0:
        curr_row, curr_col, steps = queue.pop(0)
        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))
        if curr_row == len(grid) - 1 and curr_col == len(grid[0]) - 1:
            return True
        for offset_row, offset_col in offsets:
            new_row = curr_row + offset_row
            new_col = curr_col + offset_col
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] != "#":
                    queue.append((new_row, new_col, steps + 1))
    return False


def part2(input_list: list[str]) -> str:
    grid_size = 71
    search_start = 0
    search_end = len(input_list)
    while search_end != search_start + 1:
        search_middle = (search_end + search_start) // 2
        grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
        for i in range(search_middle):
            x, y = [int(x) for x in input_list[i].split(",")]
            grid[y][x] = "#"
        if exit_exists(grid):
            search_start = search_middle
        else:
            search_end = search_middle
    return input_list[search_start]


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
