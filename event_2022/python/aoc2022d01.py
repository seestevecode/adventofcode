from pathlib import Path


def solve(input):
    calorie_totals = [sum(map(int, calories.split("\n"))) for calories in input]
    part_one = max(calorie_totals)
    part_two = sum(sorted(calorie_totals, reverse=True)[:3])
    return part_one, part_two


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.read().strip().split("\n\n")

    part_one, part_two = solve(input)

    print("Part 1:", part_one)  # 70508
    print("Part 2:", part_two)  # 208567
