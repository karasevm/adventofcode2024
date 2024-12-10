import sys

def print_grid(grid):
    for line in grid:
        for char in line:
            print(char, end='')
        print()

def find_all_tops(grid: list[list[int]], trailhead_row: int, trailhead_col: int) -> int:
    offsets = [(0,1), (1,0), (-1,0), (0, -1)]

    tops = set()
    queue = [(trailhead_row, trailhead_col)]
    while len(queue) != 0:
        curr_row, curr_col = queue.pop(0)
        curr_num = grid[curr_row][curr_col]
        if curr_num == 9:
            tops.add((curr_row, curr_col))
            continue
        for offset_row, offset_col in offsets:
            new_row = curr_row + offset_row
            new_col = curr_col + offset_col
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] == curr_num + 1:
                    queue.append((new_row, new_col))
    return len(tops)

def part1(input_list: list[str]) -> int:
    grid = []
    for line in input_list:
        grid.append([*map(int,line)])
    print_grid(grid)

    result = 0
    for row, line in enumerate(grid):
        for col, num in enumerate(line):
            if num == 0:
                result += find_all_tops(grid, row, col)

    return result

def find_all_trails(grid: list[list[int]], trailhead_row: int, trailhead_col: int) -> int:
    offsets = [(0,1), (1,0), (-1,0), (0, -1)]

    trails: set[tuple[int, int, tuple[tuple[int, int]]]] = set()
    queue = [(trailhead_row, trailhead_col, [])]
    while len(queue) != 0:
        curr_row, curr_col, history = queue.pop(0)
        curr_num = grid[curr_row][curr_col]
        if curr_num == 9:
            trails.add((curr_row, curr_col, tuple(history)))
            continue
        for offset_row, offset_col in offsets:
            new_row = curr_row + offset_row
            new_col = curr_col + offset_col
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] == curr_num + 1:
                    queue.append((new_row, new_col, history + [(curr_row, curr_col)]))
    return len(trails)

def part2(input_list: list[str]) -> int:
    grid = []
    for line in input_list:
        grid.append([*map(int,line)])

    result = 0
    for row, line in enumerate(grid):
        for col, num in enumerate(line):
            if num == 0:
                result += find_all_trails(grid, row, col)

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
