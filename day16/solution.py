import sys
from queue import PriorityQueue


def print_grid(grid, highlight=set()):
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if (i, j) in highlight:
                print("O", end="")
            else:
                print(char, end="")
        print()
    print()


def find_tile(grid: list[list[str]], tile="S") -> tuple[int, int]:
    for rown, row in enumerate(grid):
        for coln, col in enumerate(row):
            if col == tile:
                return (rown, coln)
    raise Exception("No tile found")


def find_path(grid: list[list[str]]) -> int:
    offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    queue = PriorityQueue()
    queue.put((0, *find_tile(grid), [(0, 1)]))
    while not queue.empty():
        score, curr_row, curr_col, offset_history = queue.get()
        curr_loc = grid[curr_row][curr_col]
        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))
        if curr_loc == "E":
            return score
        for offset_row, offset_col in offsets:
            new_row = curr_row + offset_row
            new_col = curr_col + offset_col
            if grid[new_row][new_col] != "#":
                if (offset_row, offset_col) == offset_history[-1]:
                    queue.put(
                        (
                            score + 1,
                            new_row,
                            new_col,
                            offset_history + [(offset_row, offset_col)],
                        )
                    )
                else:
                    queue.put(
                        (
                            score + 1001,
                            new_row,
                            new_col,
                            offset_history + [(offset_row, offset_col)],
                        )
                    )
    return -1


def part1(input_list: list[str]) -> int:
    grid: list[list[str]] = []

    for i in range(len(input_list)):
        if input_list[i] == "":
            break
        grid.append(list(input_list[i]))
    return find_path(grid)


def find_path_tiles(grid: list[list[str]]) -> int:
    offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Find move costs
    grid_costs = [[99999 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited = set()
    queue = PriorityQueue()
    queue.put((0, *find_tile(grid), [(0, 1)]))
    while not queue.empty():
        score, curr_row, curr_col, offset_history = queue.get()
        if score < grid_costs[curr_row][curr_col]:
            grid_costs[curr_row][curr_col] = score
        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))
        for offset_row, offset_col in offsets:
            new_row = curr_row + offset_row
            new_col = curr_col + offset_col
            if grid[new_row][new_col] != "#":
                if (offset_row, offset_col) == offset_history[-1]:
                    queue.put(
                        (
                            score + 1,
                            new_row,
                            new_col,
                            offset_history + [(offset_row, offset_col)],
                        )
                    )
                else:
                    queue.put(
                        (
                            score + 1001,
                            new_row,
                            new_col,
                            offset_history + [(offset_row, offset_col)],
                        )
                    )

    # Find all shortest path regardless of turns
    paths = []
    queue = [(*find_tile(grid, "E"), [])]
    while len(queue) > 0:
        curr_row, curr_col, path = queue.pop(0)
        curr_val = grid_costs[curr_row][curr_col]
        if curr_val == 0:
            path.append((curr_row, curr_col - 1)) # Account for starting facing east
            paths.append(path)
            continue
        for offset_row, offset_col in offsets:
            new_row = curr_row + offset_row
            new_col = curr_col + offset_col
            if grid_costs[new_row][new_col] % 1000 < curr_val % 1000:
                queue.append((new_row, new_col, path + [(curr_row, curr_col)]))

    end_row, end_col = find_tile(grid, "E")
    turn_count = grid_costs[end_row][end_col] // 1000

    # Among the shortest paths find those with the least amounts of turns
    tiles = set()
    for path in paths:
        path_turn_count = 0
        for i in range(len(path) - 2):
            row_a, col_a = path[i]
            row_b, col_b = path[i + 1]
            row_c, col_c = path[i + 2]
            a_b_diffs = (row_b - row_a, col_b - col_a)
            b_c_diffs = (row_c - row_b, col_c - col_b)
            if a_b_diffs != b_c_diffs:  # Moved in different direction == turn
                path_turn_count += 1
        if path_turn_count == turn_count:
            tiles |= set(path)

    return len(tiles)


def part2(input_list: list[str]) -> int:
    grid: list[list[str]] = []

    for i in range(len(input_list)):
        if input_list[i] == "":
            break
        grid.append(list(input_list[i]))

    return find_path_tiles(grid)


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
