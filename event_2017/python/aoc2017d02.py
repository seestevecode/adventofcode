from pathlib import Path


def part_one(input: list[list[int]]) -> int:
    return sum([max(row) - min(row) for row in input])


def part_two(input: list[list[int]]) -> int:
    divisors = []
    for row in input:
        divisors.append([y // x for x in row for y in row if x != y and y % x == 0])
    return sum([divisor for sublist in divisors for divisor in sublist])


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        raw_input = f.read().splitlines()

    input: list[list[int]] = [list(map(int, row.split())) for row in raw_input]

    print("Part 1:", part_one(input))  # 53460
    print("Part 2:", part_two(input))  # 282
