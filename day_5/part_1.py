import sys

if len(sys.argv) < 2:
    print("Missing input file")
    sys.exit(1)

input_file = sys.argv[1]

fresh_ranges = []
getting_ranges = True
count = 0
with open(input_file) as f:
    for line in f:
        if line == "\n":
            getting_ranges = False
            continue
        if getting_ranges:
            start, end = line.strip().split("-")
            fresh_ranges.append((int(start), int(end)))
        else:
            print('ranges',fresh_ranges)
            ingredient = int(line.strip())
            for r in fresh_ranges:
                if ingredient >= r[0] and ingredient <= r[1]:
                    count += 1
                    break

print(f"Availbale fresh ingredients {count}")


