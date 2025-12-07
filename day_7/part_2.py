from os import truncate
import pprint
import sys

def main():
    if len(sys.argv) < 2:
        print("Missing input file argument")
        sys.exit(1)

    input_file = sys.argv[1]

    grid = []
    col_start = -1
    with open(input_file) as f:
        for line in f:
            if col_start == -1:
                col_start = int(line.find("S"))
            grid.append(line)

    result_map = [[-1 for _ in grid[0]] for _ in grid]

    def count_timelines(row: int, col: int, grid: list[str]) -> int:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0

        if result_map[row][col] != -1:
            return result_map[row][col]

        count = 1
        for i in range(row + 1, len(grid)):
            if grid[i][col] == '^':
                left = count_timelines(i, col - 1, grid)
                right = count_timelines(i, col + 1, grid)
                count = left + right
                break

        result_map[row][col] = count
        return count

    timelines = count_timelines(0, col_start, grid)
    print(f"Timelines: {timelines}")


if __name__ == "__main__":
    main()
