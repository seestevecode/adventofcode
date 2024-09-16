from pathlib import Path


def solve():
    paper, ribbon = 0, 0
    for dim_string in input:
        dims = sorted([int(dim) for dim in dim_string.split("x")])
        paper += (
            2 * (dims[0] * dims[1] + dims[1] * dims[2] + dims[2] * dims[0])
            + dims[0] * dims[1]
        )
        ribbon += 2 * (dims[0] + dims[1]) + dims[0] * dims[1] * dims[2]
    return (paper, ribbon)


def part_one():
    return solve()[0]


def part_two():
    return solve()[1]


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.read().strip().splitlines()

    print("Part 1:", part_one())  # 1586300
    print("Part 2:", part_two())  # 3737498
