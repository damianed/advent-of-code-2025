import sys
import pprint

class RedTile:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __repr__(self):
        return f"Tile({self.col}, {self.row})"

def print_map(inside_points: list[tuple]):
    m = []
    for row in range(len(inside_points)):
        m.append([])
        for col in range(0, inside_points[row][1] + 1):
            if col >= inside_points[row][0] and col <= inside_points[row][1]:
                m[row].append('#')
            else:
                m[row].append(".")

    pprint.pp(m)

def calculate_area(tile1: RedTile, tile2: RedTile) -> int:
    height = abs(tile2.row - tile1.row) + 1
    width = abs(tile2.col - tile1.col) + 1
    area = height * width
    print(f"{tile1} - {tile2} = {area}")
    return area

def fill_up_line(start: RedTile, end: RedTile, inside_points: list[tuple], min_row: int):
    print(f"computing {start} to {end}")
    if start.row == end.row:
        begin, to = (start.col, end.col) if start.col < end.col else (end.col, start.col)
        adjusted_row = start.row - min_row
        min_col, max_col = inside_points[adjusted_row]
        if begin < min_col:
            min_col = begin
        if to > max_col:
            max_col =  to
        inside_points[adjusted_row] = (min_col, max_col)
        print(f'updating row {adjusted_row} - min {min_col} - max {max_col}')
    elif start.col == end.col:
        begin, to = (start.row, end.row) if start.row < end.row else (end.row, start.row)
        for i in range(begin, to + 1):
            adjusted_row = i - min_row
            min_col, max_col = inside_points[adjusted_row]
            min_col = min(start.col, min_col)
            max_col = max(start.col, max_col)
            print(f'updating row {adjusted_row} - min {min_col} - max {max_col}')
            inside_points[adjusted_row] = (min_col, max_col)

def is_inside_points(tile1: RedTile, tile2: RedTile, inside_points: list[tuple], min_row: int) -> bool:
    corner1 = (tile1.row - min_row, tile2.col)
    corner2 = (tile2.row - min_row, tile1.col)

    if inside_points[corner1[0]][0] > corner1[1] or inside_points[corner1[0]][1] < corner1[1]:
        #First corner outside area
        return False

    if inside_points[corner2[0]][0] > corner2[1] or inside_points[corner2[0]][1] < corner2[1]:
        #second corner outside area
        return False

    return True

def main(input_file):
    red_tiles = []
    min_row, max_row = (2**31)-1, -1
    with open(input_file) as f:
        for line in f:
            col, row = line.strip().split(',')
            row, col = int(row), int(col)
            min_row = min(min_row, row)
            max_row = max(max_row, row)
            tile = RedTile(row, col)
            red_tiles.append(tile)


    # (min, max) of each row
    inside_points = [((2**31) - 1, -1) for _ in range(max_row - min_row + 1)]

    print("min_row", min_row)
    prev = None
    for tile in red_tiles:
        if prev:
            fill_up_line(prev, tile, inside_points, min_row)
        prev = tile

    assert(prev)
    fill_up_line(prev, red_tiles[0], inside_points, min_row)
    max_area = 0
    print("min - max", min_row, max_row)

    for i, tile1 in enumerate(red_tiles):
        for j in range(i+1, len(red_tiles)):
            tile2 = red_tiles[j]
            if is_inside_points(tile1, tile2, inside_points, min_row):
                max_area = max(max_area, calculate_area(tile1, tile2))

    #print_map(inside_points)

    print(f"max area {max_area}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Missing input file")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
