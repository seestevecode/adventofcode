from pathlib import Path


def answer_part(part):
    paper, ribbon = 0, 0
    for dim_string in input:
        dims = sorted([int(dim) for dim in dim_string.split("x")])
        paper += (
            2 * (dims[0] * dims[1] + dims[1] * dims[2] + dims[2] * dims[0])
            + dims[0] * dims[1]
        )
        ribbon += 2 * (dims[0] + dims[1]) + dims[0] * dims[1] * dims[2]
    return paper if part == 1 else ribbon


if __name__ == "__main__":
    # import input
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.read().strip().splitlines()

    # results
    print("Part 1:", answer_part(1))
    print("Part 2:", answer_part(2))
