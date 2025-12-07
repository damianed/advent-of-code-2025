import sys

def cepha_nums_to_human(cepha_nums: list[str]) -> list[int]:
    res = []
    for num in cepha_nums:
        for i in range(len(num)):
            if i >= len(res):
                res.append([])
            res[i].append(num[i])

    res = [int("".join(r).strip()) for r in res]
    return res

def main():
    if len(sys.argv) < 2:
        exit(1)

    input_file = sys.argv[1]

    operations = []
    max_length_group = [0]
    lines = []
    with open(input_file) as f:
        for line in f:
            if "+" in line or "*" in line:
                operations = line.strip().split()
                break

            ns = line.strip().split()
            for i in range(len(ns)):
                if i >= len(max_length_group):
                    max_length_group.append(0)
                max_length_group[i] = max(max_length_group[i], len(ns[i]))
            lines.append(line)

    nums = [[] for _ in range(len(max_length_group))]
    for line in lines:
        found_first_digit = False
        current_group = 0
        curr_num = []
        for i in range(len(line)):
            c = line[i]
            if c == '\n':
                c = ' '

            if found_first_digit and c == ' ' and len(curr_num) == max_length_group[current_group]:
                found_first_digit = False
                nums[current_group].append(curr_num.copy())
                curr_num = []
                current_group += 1
                continue

            if c != ' ':
                found_first_digit = True

            curr_num.append(c)

        if current_group < len(nums):
            nums[current_group].append(curr_num)

    total = 0
    human_nums = []
    for c_nums in nums:
        human_nums.append(cepha_nums_to_human(c_nums))

    for i, op in enumerate(operations):
        loc_total = 0 if op == "+" else 1
        for n in human_nums[i]:
            if op == "+":
                loc_total += n
            else:
                loc_total *= n

        total += loc_total

    print(f"total {total}")


if __name__ == "__main__":
    main()

