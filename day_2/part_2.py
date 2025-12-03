import sys

def is_same(n: int) -> bool:
    strn = str(n)

    i = 0
    curr_len = 1
    while i + curr_len < len(strn):
        if strn[i] == strn[i + curr_len]:
            i += 1
        else:
            i = 0
            curr_len += 1

    return i > 0 and len(strn) % curr_len == 0

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
