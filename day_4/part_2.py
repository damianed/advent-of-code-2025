import sys
import collections

def can_be_accessed(row: int, col: int, grid: list[list[str]], adjacent_map: list[list[int]]) -> bool:
    adjacent_rolls = 0
    directions  = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    for d in directions:
        checkRow = row + d[0]
        checkCol = col + d[1]

        if checkRow >= 0 and checkRow < len(grid) and checkCol >= 0 and checkCol < len(grid[row]):
            if grid[checkRow][checkCol] == '@':
                adjacent_rolls += 1

    adjacent_map[row][col] = adjacent_rolls

    return adjacent_rolls < 4


def get_adjacent_removals(row: int, col: int, grid: list[list[str]], adjacent_map: list[list[int]]) -> int:
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return 0

    queue = collections.deque([(row, col)])
    directions  = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    count = 0
    while queue:
        r, c = queue.popleft()
        for d in directions:
            a_row = r + d[0]
            a_col = c + d[1]
            if 0 <= a_row < len(grid) and 0 <= a_col < len(grid[0]) and grid[a_row][a_col] == '@' and adjacent_map[a_row][a_col] != -1:
                adjacent_map[a_row][a_col] -= 1
                if adjacent_map[a_row][a_col] < 4:
                    count += 1
                    queue.append((a_row, a_col))
                    grid[a_row][a_col] = '.'
    return count


def get_removable_count(row, col, grid, adjacent_map) -> int:
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '.':
        return 0

    count = 0
    if can_be_accessed(row, col, grid, adjacent_map):
        grid[row][col] = '.'
        count += 1
        count += get_adjacent_removals(row, col, grid, adjacent_map)

    return count

def main():
    if len(sys.argv) < 2:
        print("Missing input file")
        sys.exit(1)

    file = sys.argv[1]
    grid = []
    with open(file) as f:
        for line in f:
            grid.append(list(line.strip()))


    count = 0
    adjacent_map = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                count += get_removable_count(row, col, grid, adjacent_map)

    print(f"Rolls that can be accessed: {count}")


if __name__ == "__main__":
    main()
