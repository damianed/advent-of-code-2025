import sys

def get_max_joltage(battery_bank: str) -> int:
    tens = 0
    units = 0
    for i in range(len(battery_bank)):
        num = int(battery_bank[i])
        if num > tens and i < len(battery_bank) - 1:
            tens = num
            units = int(battery_bank[i + 1])
        elif num > units:
            units = num


    return (tens * 10) + units

def main():
    if len(sys.argv) < 2:
        print("Missing input file")
        sys.exit(1)

    input_file = sys.argv[1]

    total = 0
    with open(input_file) as f:
        for line in f:
            total += get_max_joltage(line.strip())

    print(f"Result {total}")


if __name__ == "__main__":
    main()
