import sys

def get_max_joltage(battery_bank: str, turn_amount = 12) -> int:
    turned_on = [-1] * turn_amount
    last_index = 0

    for j in range(turn_amount):
        for i in range(last_index, len(battery_bank) - (turn_amount - 1) + j):
            num = int(battery_bank[i])
            if num > turned_on[j]:
                turned_on[j] = num
                last_index = i + 1

    curr_battery = len(battery_bank) - 1
    for i in range(len(turned_on) - 1, -1, -1):
        if turned_on[i] != -1:
            break

        turned_on[i] = int(battery_bank[curr_battery])
        curr_battery -= 1

    total = 0
    pos_value = 1
    for i in range(len(turned_on) -1, -1, -1):
        total += turned_on[i] * pos_value
        pos_value *= 10

    return total

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
