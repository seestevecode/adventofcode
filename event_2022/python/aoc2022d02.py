from pathlib import Path

SCORES = {
    ("A", "X"): (4, 3),
    ("A", "Y"): (8, 4),
    ("A", "Z"): (3, 8),
    ("B", "X"): (1, 1),
    ("B", "Y"): (5, 5),
    ("B", "Z"): (9, 9),
    ("C", "X"): (7, 2),
    ("C", "Y"): (2, 6),
    ("C", "Z"): (6, 7),
}


def solve(input):
    part_one = sum(SCORES[game][0] for game in input)
    part_two = sum(SCORES[game][1] for game in input)
    return (part_one, part_two)


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = list(map(lambda x: tuple(x.split()), f.read().strip().split("\n")))

    part_one, part_two = solve(input)

    print("Part 1:", part_one)  # 11603
    print("Part 2:", part_two)  # 12725
