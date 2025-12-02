import sys

if len(sys.argv) < 2:
    raise IndexError("Missing required argument: filename")

input_file = sys.argv[1]
current_value = 50
max_value = 99
password = 0

with open(input_file, "r") as f:
    for line in f:
        if line.strip() == "":
            continue

        direction = line[0]
        amount = int(line[1:].strip())

        if direction == 'L':
            prev = current_value
            current_value = current_value - amount
            if prev != 0 and current_value <= 0:
                password += 1

            password += abs(current_value) // (max_value + 1)
            if current_value < 0:
                current_value = current_value % (max_value + 1)

        if direction == 'R':
            current_value = current_value + amount
            password += current_value // (max_value + 1)
            if current_value > max_value:
                current_value = current_value % (max_value + 1)


print(f"Password: {password}")

