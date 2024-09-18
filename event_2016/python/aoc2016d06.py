from pathlib import Path
from collections import Counter


def solve() -> tuple[str, str]:
    code_one, code_two = [], []
    for group in list(zip(*input)):
        most_common = Counter(group).most_common()
        least_common = sorted(most_common, key=lambda x: x[1])
        code_one.append(most_common[0][0])
        code_two.append(least_common[0][0])
    return "".join(code_one), "".join(code_two)


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.read().splitlines()

    part_one, part_two = solve()

    print("Part 1:", part_one)  # ursvoerv
    print("Part 2:", part_two)  # vomaypnn
