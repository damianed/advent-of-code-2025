import sys

if len(sys.argv) < 2:
    print("Missing file argument")
    exit(1)

input_file = sys.argv[1]

nums = []
operations = []
with open(input_file) as f:
    for line in f:
        if "+" in line or "*" in line:
            operations = line.strip().split()
            break

        numbers = line.strip().split()
        for i in range(len(numbers)):
            if i > len(nums) - 1:
                nums.append([])
            nums[i].append(int(numbers[i]))

total = 0
for i, op in enumerate(operations):
    loc_total = 0 if op == "+" else 1
    for n in nums[i]:
        if op == "+":
            loc_total += n
        else:
            loc_total *= n

    total += loc_total

print(f"total {total}")


