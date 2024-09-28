from pathlib import Path

NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def solve(input):
    checksum_one, checksum_two = 0, 0
    for line in input:
        digits_one, digits_two = [], []
        for line_idx, char in enumerate(line):
            if char.isdigit():
                digits_one.append(char)
                digits_two.append(char)
                continue
            for num_idx, num in enumerate(NUMBERS):
                if line[line_idx:].startswith(num):
                    digits_two.append(str(num_idx + 1))
        checksum_one += int(digits_one[0] + digits_one[-1])
        checksum_two += int(digits_two[0] + digits_two[-1])
    return checksum_one, checksum_two


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.readlines()

    parsed_input = [row.strip() for row in input]

    print("Part 1:", solve(parsed_input)[0])  # 53334
    print("Part 2:", solve(parsed_input)[1])  # 52834
