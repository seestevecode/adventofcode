from pathlib import Path


def part_two():
    level = 0
    for idx, char in enumerate(input, start=1):
        level = level - 1 if char == ")" else level + 1
        if level == -1:
            return idx


if __name__ == "__main__":
    # import input
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.read()

    # results
    print("Part 1:", input.count("(") - input.count(")"))  # 280
    print("Part 2:", part_two())  # 1797
