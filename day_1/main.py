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
            current_value = current_value - int(line[1:].strip())
            while current_value < 0:
                current_value = max_value - (current_value * -1) + 1

        if direction == 'R':
            current_value = current_value + int(line[1:].strip())
            while current_value > max_value:
                current_value = current_value - max_value - 1

        if current_value == 0:
            password += 1

print(f"Password: {password}")

