from pathlib import Path


def part_one():
    pass


def part_two():
    pass


if __name__ == "__main__":
    # import input
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.read()

    # results
    print("Part 1:", part_one())
    print("Part 2:", part_two())
