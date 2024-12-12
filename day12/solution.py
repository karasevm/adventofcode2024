import sys


def print_grid(grid):
    for line in grid:
        for char in line:
            print(char, end="")
        print()


class Region:

    def __init__(
        self,
        coords: list[tuple[int, int]],
        perimeter: int,
        area: int,
        type: str,
        sides=0,
    ):
        self.perimeter = perimeter
        self.area = area
        self.coords = tuple(coords)
        self.type = type
        self.sides = sides
        pass

    def __hash__(self) -> int:
        return hash((self.area, self.perimeter, self.coords))

    def includes_coord(self, row: int, col: int) -> bool:
        try:
            _ = self.coords.index((row, col))
            return True
        except:
            return False

    def get_cost(self):
        return self.area * self.perimeter

    def get_cost_sides(self):
        return self.area * self.sides


def calc_region_with_sides(grid: list[list[str]], row: int, col: int):
    offsets = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    queue = [(row, col)]
    plot_type = grid[row][col]
    area = 0
    perimeter = 0
    visited = set()
    fences = set()
    while len(queue) != 0:
        curr_row, curr_col = queue.pop(0)
        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))
        area += 1
        for offset_row, offset_col in offsets:
            new_row = curr_row + offset_row
            new_col = curr_col + offset_col
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] == plot_type:
                    queue.append((new_row, new_col))
                else:
                    fences.add(((curr_row, curr_col, new_row, new_col)))
                    perimeter += 1
            else:
                fences.add(((curr_row, curr_col, new_row, new_col)))
                perimeter += 1

    # Go over all the fences, if a fence is near another fence increase the neighbor count
    neighbor = 0
    fences = list(fences)
    i = 0
    while i < len(fences):
        plot_a_row, plot_a_col, plot_b_row, plot_b_col = fences[i]
        j = i + 1
        while j < len(fences):
            new_plot_a_row, new_plot_a_col, new_plot_b_row, new_plot_b_col = fences[j]
            # Fence is 1 row or 1 col away
            if (
                plot_a_col == new_plot_a_col
                and abs(plot_a_row - new_plot_a_row) == 1
                and plot_b_col == new_plot_b_col
                and abs(plot_b_row - new_plot_b_row) == 1
            ) or (
                plot_a_row == new_plot_a_row
                and abs(plot_a_col - new_plot_a_col) == 1
                and plot_b_row == new_plot_b_row
                and abs(plot_b_col - new_plot_b_col) == 1
            ):
                neighbor += 1
            j += 1
        i += 1
    return (area, perimeter, visited, len(fences) - neighbor)


def part1(input_list: list[str]) -> int:
    grid = []
    for line in input_list:
        grid.append(list(line))
    # print_grid(grid)
    regions: list[Region] = []

    for row, line in enumerate(grid):
        for col, plot in enumerate(line):
            if any([x.includes_coord(row, col) for x in regions]):
                continue
            area, perimeter, visited, sides = calc_region_with_sides(grid, row, col)
            regions.append(Region(list(visited), perimeter, area, plot, sides))

    result = sum([x.get_cost() for x in regions])

    return result


def part2(input_list: list[str]) -> int:
    grid = []
    for line in input_list:
        grid.append(list(line))
    # print_grid(grid)
    regions: list[Region] = []

    for row, line in enumerate(grid):
        for col, plot in enumerate(line):
            if any([x.includes_coord(row, col) for x in regions]):
                continue
            area, perimeter, visited, sides = calc_region_with_sides(grid, row, col)
            regions.append(Region(list(visited), perimeter, area, plot, sides))

    result = sum([x.get_cost_sides() for x in regions])
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
