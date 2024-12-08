import sys


def part1(input_list: list[str]) -> int:

    grid = []
    for line in input_list:
        grid.append(list(line))

    antinodes = set()

    for row_number, row in enumerate(grid):
        for col_number, col in enumerate(row):
            if col != ".":
                for row2_number, row2 in enumerate(grid):
                    for col2_number, col2 in enumerate(row2):
                        if col2 == col and not (
                            row_number == row2_number and col_number == col2_number
                        ):
                            new_antinode_a = (
                                row_number - row2_number + row_number,
                                col_number - col2_number + col_number,
                            )
                            new_antinode_b = (
                                -(row_number - row2_number) + row2_number,
                                -(col_number - col2_number) + col2_number,
                            )
                            if (
                                new_antinode_a[0] >= 0
                                and new_antinode_a[0] < len(grid)
                                and new_antinode_a[1] >= 0
                                and new_antinode_a[1] < len(grid[0])
                            ):
                                antinodes.add((new_antinode_a))
                            if (
                                new_antinode_b[0] >= 0
                                and new_antinode_b[0] < len(grid)
                                and new_antinode_b[1] >= 0
                                and new_antinode_b[1] < len(grid[0])
                            ):
                                antinodes.add((new_antinode_b))

    return len(antinodes)


def part2(input_list: list[str]) -> int:

    grid = []
    for line in input_list:
        grid.append(list(line))

    antinodes = set()

    for row_number, row in enumerate(grid):
        for col_number, col in enumerate(row):
            if col != ".":
                for row2_number, row2 in enumerate(grid):
                    for col2_number, col2 in enumerate(row2):
                        if col2 == col and not (
                            row_number == row2_number and col_number == col2_number
                        ):
                            offset_a = (
                                row_number - row2_number,
                                col_number - col2_number,
                            )
                            offset_b = (
                                -(row_number - row2_number),
                                -(col_number - col2_number),
                            )

                            offset_mult = 0
                            while True:
                                offset_mult += -1
                                if (
                                    offset_a[0] * offset_mult + row_number >= 0
                                    and offset_a[0] * offset_mult + row_number
                                    < len(grid)
                                    and offset_a[1] * offset_mult + col_number >= 0
                                    and offset_a[1] * offset_mult + col_number
                                    < len(grid[0])
                                ):
                                    antinodes.add(
                                        (
                                            offset_a[0] * offset_mult + row_number,
                                            offset_a[1] * offset_mult + col_number,
                                        )
                                    )
                                    continue
                                break

                            offset_mult = 0
                            while True:
                                offset_mult += -1
                                if (
                                    offset_b[0] * offset_mult + row2_number >= 0
                                    and offset_b[0] * offset_mult + row2_number
                                    < len(grid)
                                    and offset_b[1] * offset_mult + col2_number >= 0
                                    and offset_b[1] * offset_mult + col2_number
                                    < len(grid[0])
                                ):
                                    antinodes.add(
                                        (
                                            offset_b[0] * offset_mult + row2_number,
                                            offset_b[1] * offset_mult + col2_number,
                                        )
                                    )
                                    continue
                                break

    return len(antinodes)


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
