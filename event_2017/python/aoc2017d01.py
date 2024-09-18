from pathlib import Path


def solve(offset):
    return sum(
        [
            int(digit)
            for idx, digit in enumerate(input)
            if input[idx] == input[(idx + offset) % len(input)]
        ]
    )


def part_one():
    return solve(1)


def part_two():
    return solve(len(input) // 2)


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.read().strip("\n")

    print("Part 1:", part_one())  # 1390
    print("Part 2:", part_two())  # 1232
