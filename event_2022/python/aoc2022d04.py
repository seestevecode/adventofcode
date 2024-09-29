from pathlib import Path


def solve(input):
    subsets, overlaps = 0, 0
    for row in input:
        str1, str2 = row.split(",")
        start1, end1 = map(int, str1.split("-"))
        start2, end2 = map(int, str2.split("-"))
        range1, range2 = range(start1, end1 + 1), range(start2, end2 + 1)
        if set(range1).issubset(range2) or set(range2).issubset(range1):
            subsets += 1
        if start1 <= end2 and start2 <= end1:
            overlaps += 1
    return subsets, overlaps


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.read().strip().split("\n")

    part_one, part_two = solve(input)

    print("Part 1:", part_one)  # 424
    print("Part 2:", part_two)  # 804
