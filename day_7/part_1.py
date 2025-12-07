import sys

def main():
    if len(sys.argv) < 2:
        print("Missing input file argument")
        sys.exit(1)

    input_file = sys.argv[1]
    ray_map = []

    split_count = 0
    with open(input_file) as f:
        for line in f:
            if len(ray_map) == 0:
                ray_map = [False for _ in line]

            for i, c in enumerate(line):
                if c == '.':
                    continue

                if c == 'S':
                    ray_map[i] = True

                if c == '^' and ray_map[i]:
                    split_count += 1
                    ray_map[i] = False
                    if i > 0:
                        ray_map[i - 1] = True
                    if i < len(ray_map):
                        ray_map[i + 1] = True


    print(f"res {split_count}")

if __name__ == "__main__":
    main()
