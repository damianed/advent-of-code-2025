import sys

if len(sys.argv) < 2:
    print("Missing input file")
    sys.exit(1)

input_file = sys.argv[1]

fresh_ranges = []
with open(input_file) as f:
    for line in f:
        if line == "\n":
            break

        start, end = line.strip().split("-")
        fresh_ranges.append((int(start), int(end)))

fresh_ranges.sort()

count = 0
next_start = fresh_ranges[0][0]
next_end = fresh_ranges[0][1]
i = 0
while i < len(fresh_ranges):
    count += next_end - next_start + 1

    i += 1
    if i < len(fresh_ranges):
        prev_end = next_end
        next_end = fresh_ranges[i][1]

        while next_end <= prev_end:
            i += 1
            next_end = fresh_ranges[i][1]

        next_start = fresh_ranges[i][0]

        if i < len(fresh_ranges) and prev_end >= next_start:
            next_start = prev_end + 1


print(f"Availbale fresh ingredients {count}")


