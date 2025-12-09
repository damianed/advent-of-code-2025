import sys

class RedTile:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __repr__(self):
        return f"Tile({self.col}, {self.row})"

def calculate_area(tile1: RedTile, tile2: RedTile) -> int:
    height = abs(tile2.row - tile1.row) + 1
    width = abs(tile2.col - tile1.col) + 1

    return height * width

def main(input_file):
    red_tiles = []
    with open(input_file) as f:
        for line in f:
            col, row = line.strip().split(',')

            red_tiles.append(RedTile(int(row), int(col)))

    max_area = 0

    for i, tile1 in enumerate(red_tiles):
        for j in range(i+1, len(red_tiles)):
            tile2 = red_tiles[j]
            max_area = max(max_area, calculate_area(tile1, tile2))

    print(f"max area {max_area}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
