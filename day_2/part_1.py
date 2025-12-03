import sys

def is_same(n: int) -> bool:
    strn = str(n)
    if len(strn) % 2 != 0:
        return False

    mid = len(strn) // 2
    first = strn[:mid]
    second = strn[mid:]

    return first == second

def main():
    if len(sys.argv) < 2:
        raise IndexError("Missing required argument: filename")

    input_file = sys.argv[1]

    ranges = []
    with open(input_file) as f:
        for line in f:
            range_strings = line.strip().split(',')
            ranges = [string.split('-') for string in range_strings]

    total = 0
    for r in ranges:
        for n in range(int(r[0]), int(r[1]) + 1):
            if is_same(n):
                total += n
    print(f"Result: {total}")

if __name__ == '__main__':
    main()
