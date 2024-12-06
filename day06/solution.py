import sys
import copy


def get_visited_coords(grid):
    directions = ['^', '>', 'v', '<']
    offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_row, curr_col = 0, 0
    direction = '^'

    for row_n, row in enumerate(grid):
        for col_n, col in enumerate(row):   
            if col in directions:
                curr_row = row_n
                curr_col = col_n
                direction = col
    visited = set()
    visited.add((curr_row, curr_col))
    while True:
        drow, dcol = offsets[directions.index(direction)]
        
        if curr_row+drow >= len(grid) or curr_row+drow < 0 or curr_col+dcol >= len(grid[0]) or curr_col+dcol < 0:
            break
        if grid[curr_row+drow][curr_col+dcol]=='#':
            direction = directions[(directions.index(direction)+1)%4]
            continue
        visited.add((curr_row+drow, curr_col+dcol))
        curr_row += drow
        curr_col += dcol
    return visited

def part1(input_list: list[str]) -> int:
    grid = []
    for line in input_list:
        grid.append(list(line))
    visited = get_visited_coords(grid)
    return len(visited)

def is_looping(grid):
    directions = ['^', '>', 'v', '<']
    offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    curr_row, curr_col, direction = 0, 0, '^'

    for row_n, row in enumerate(grid):
        for col_n, col in enumerate(row):   
            if col in directions:
                curr_row = row_n
                curr_col = col_n
                direction = col

    visited = set()
    while True:
        drow, dcol = offsets[directions.index(direction)]
        
        if curr_row+drow >= len(grid) or curr_row+drow < 0 or curr_col+dcol >= len(grid[0]) or curr_col+dcol < 0:
            return False
        if grid[curr_row+drow][curr_col+dcol]=='#':
            direction = directions[(directions.index(direction)+1)%4]
        else:  
            curr_row += drow
            curr_col += dcol
        if (curr_row, curr_col, direction) in visited:
            return True
        visited.add((curr_row, curr_col, direction))



def part2(input_list: list[str]) -> int:
    success_count = 0
    grid = []
    for line in input_list:
        grid.append(list(line))

    coords_to_check = get_visited_coords(grid)

    for row_n, col_n in coords_to_check:
        new_grid = copy.deepcopy(grid)
        new_grid[row_n][col_n] = '#'
        success_count += is_looping(new_grid)
    return success_count

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
