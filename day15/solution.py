import sys
from copy import deepcopy


def print_grid(grid):
    for line in grid:
        for char in line:
            print(char, end="")
        print()
    print()


def attempt_to_move(
    grid: list[list[str]], row_to_move: int, col_to_move: int, direction
) -> list[list[str]]:
    dir_map = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

    offset_row, offset_col = dir_map[direction]

    new_row = row_to_move + offset_row
    new_col = col_to_move + offset_col
    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
        match grid[new_row][new_col]:
            case ".":
                grid[new_row][new_col] = grid[row_to_move][col_to_move]
                grid[row_to_move][col_to_move] = "."
                return grid
            case "#":
                raise Exception("Hit wall")
            case "O":
                grid = attempt_to_move(grid, new_row, new_col, direction)
                if grid[new_row][new_col] == ".":
                    grid[new_row][new_col] = grid[row_to_move][col_to_move]
                    grid[row_to_move][col_to_move] = "."
            case _:
                print("Unexpected input")
    else:
        raise Exception("Out of bounds")
    return grid


def find_robot(grid: list[list[str]]) -> tuple[int, int]:
    for rown, row in enumerate(grid):
        for coln, col in enumerate(row):
            if col == "@":
                return (rown, coln)
    raise Exception("No robot found")


def part1(input_list: list[str]) -> int:
    grid: list[list[str]] = []

    movements = []
    i = 0
    while i < len(input_list):
        if input_list[i] == "":
            break
        grid.append(list(input_list[i]))
        i += 1

    grid = grid[1:-1]
    for j in range(len(grid)):
        grid[j] = grid[j][1:-1]

    while i < len(input_list):
        movements.extend(list(input_list[i]))
        i += 1
    for movement in movements:
        robot_row, robot_col = find_robot(grid)
        try:
            grid = attempt_to_move(grid, robot_row, robot_col, movement)
        except:
            pass
    result = 0

    for rown, row in enumerate(grid):
        for coln, col in enumerate(row):
            if col == "O":
                result += (rown + 1) * 100 + coln + 1
    return result


def attempt_to_wide_move(
    grid: list[list[str]], row_to_move: int, col_to_move: int, direction
) -> list[list[str]]:
    dir_map = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

    offset_row, offset_col = dir_map[direction]

    new_row = row_to_move + offset_row
    new_col = col_to_move + offset_col
    if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
        if direction in (">", "<"):
            match grid[new_row][new_col]:
                case ".":
                    grid[new_row][new_col] = grid[row_to_move][col_to_move]
                    grid[row_to_move][col_to_move] = "."
                    return grid
                case "#":
                    raise Exception("Hit wall")
                case "[" | "]":
                    grid = attempt_to_wide_move(grid, new_row, new_col, direction)
                    if grid[new_row][new_col] == ".":
                        grid[new_row][new_col] = grid[row_to_move][col_to_move]
                        grid[row_to_move][col_to_move] = "."
                case _:
                    print("Unexpected input")
        else:
            match grid[new_row][new_col]:
                case ".":
                    grid[new_row][new_col] = grid[row_to_move][col_to_move]
                    grid[row_to_move][col_to_move] = "."
                    return grid
                case "#":
                    raise Exception("Hit wall")
                case "[":
                    tmp_grid = deepcopy(grid)
                    tmp_grid = attempt_to_wide_move(
                        tmp_grid, new_row, new_col, direction
                    )
                    tmp_grid = attempt_to_wide_move(
                        tmp_grid, new_row, new_col + 1, direction
                    )

                    if tmp_grid[new_row][new_col] == ".":
                        grid = tmp_grid
                        grid[new_row][new_col] = grid[row_to_move][col_to_move]
                        grid[row_to_move][col_to_move] = "."
                case "]":
                    tmp_grid = deepcopy(grid)
                    tmp_grid = attempt_to_wide_move(
                        tmp_grid, new_row, new_col, direction
                    )
                    tmp_grid = attempt_to_wide_move(
                        tmp_grid, new_row, new_col - 1, direction
                    )
                    if tmp_grid[new_row][new_col] == ".":
                        grid = tmp_grid
                        grid[new_row][new_col] = grid[row_to_move][col_to_move]
                        grid[row_to_move][col_to_move] = "."

                case _:
                    print("Unexpected input")
    else:
        raise Exception("Box hit edge")
    return grid


def part2(input_list: list[str]) -> int:
    grid: list[list[str]] = []

    grid_map = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    movements = []
    i = 0
    while i < len(input_list):
        if input_list[i] == "":
            break
        tmp_line = []
        for tile in input_list[i]:
            tmp_line.extend(grid_map[tile])
        grid.append(tmp_line)
        i += 1

    grid = grid[1:-1]
    for j in range(len(grid)):
        grid[j] = grid[j][2:-2]

    while i < len(input_list):
        movements.extend(list(input_list[i]))
        i += 1

    for movement in movements:
        robot_row, robot_col = find_robot(grid)
        try:
            grid = attempt_to_wide_move(grid, robot_row, robot_col, movement)
        except:
            pass
    result = 0

    for rown, row in enumerate(grid):
        for coln, col in enumerate(row):
            if col == "[":
                result += (rown + 1) * 100 + coln + 2

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
