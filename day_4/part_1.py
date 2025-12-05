import sys

def can_be_accessed(row: int, col: int, grid: list[str]) -> bool:
    adjacent_rolls = 0
    directions  = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    for d in directions:
        checkRow = row + d[0]
        checkCol = col + d[1]

        if checkRow >= 0 and checkRow < len(grid) and checkCol >= 0 and checkCol < len(grid[row]):
            if grid[checkRow][checkCol] == '@':
                adjacent_rolls += 1
                if adjacent_rolls >= 4:
                    return False

    return True

def main():
    if len(sys.argv) < 2:
        print("Missing input file")
        sys.exit(1)

    file = sys.argv[1]
    grid = []
    with open(file) as f:
        for line in f:
            grid.append(line.strip())


    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@' and can_be_accessed(row, col, grid):
                count += 1

    print(f"Rolls that can be accessed: {count}")

if __name__ == "__main__":
    main()
