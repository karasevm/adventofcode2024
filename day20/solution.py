import sys


def find_tile(grid: list[list[str]], tile="S") -> tuple[int, int]:
    for rown, row in enumerate(grid):
        for coln, col in enumerate(row):
            if col == tile:
                return (rown, coln)
    raise Exception("No tile found")


def solve(grid: list[list[str]], limit) -> int:
    offsets = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    grid_costs = [[99999 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited = set()
    queue = [(0, *find_tile(grid, "E"))]
    while len(queue) != 0:
        score, curr_row, curr_col = queue.pop(0)
        if score < grid_costs[curr_row][curr_col]:
            grid_costs[curr_row][curr_col] = score
        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))
        for offset_row, offset_col in offsets:
            new_row = curr_row + offset_row
            new_col = curr_col + offset_col
            if grid[new_row][new_col] != "#":
                queue.append((score + 1, new_row, new_col))

    cheat_diffs_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            curr_tile = grid_costs[row][col]
            if curr_tile != 99999:
                queue = [(row, col, [])]
                visited = set()
                while len(queue) != 0:
                    curr_row, curr_col, path = queue.pop(0)
                    if (curr_row, curr_col) in visited:
                        continue
                    visited.add((curr_row, curr_col))
                    if len(path) >= limit + 1:
                        continue
                    if grid_costs[curr_row][curr_col] != 99999:
                        diff = grid_costs[curr_row][curr_col] - curr_tile - len(path)
                        if diff >= 100:
                            cheat_diffs_count += 1
                    for offset_row, offset_col in offsets:
                        new_row = curr_row + offset_row
                        new_col = curr_col + offset_col
                        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                            queue.append((new_row, new_col, path + [(new_row, new_col)]))
    return cheat_diffs_count


def part1(input_list: list[str]) -> int:
    grid: list[list[str]] = []

    for line in input_list:
        grid.append(list(line))

    return solve(grid, 2)


def part2(input_list: list[str]) -> int:
    grid: list[list[str]] = []

    for line in input_list:
        grid.append(list(line))

    return solve(grid, 20)


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
