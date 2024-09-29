from pathlib import Path

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def priority(item):
    priority = ALPHABET.index(item.lower()) + 1
    return priority if item in ALPHABET else priority + 26


def part_one(input):
    total_score = 0
    for rucksack in input:
        mid = len(rucksack) // 2
        compartment1, compartment2 = rucksack[:mid], rucksack[mid:]
        mistake = list(set(compartment1).intersection(compartment2))[0]
        total_score += priority(mistake)
    return total_score


def part_two(input):
    total_score = 0
    groups = [list(group) for group in zip(*[iter(input)] * 3)]
    for rucksack_group in groups:
        rucksack1, rucksack2, rucksack3 = rucksack_group
        badge = list(set(rucksack1).intersection(rucksack2).intersection(rucksack3))[0]
        total_score += priority(badge)
    return total_score


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.read().strip().split("\n")

    print("Part 1:", part_one(input))  # 8252
    print("Part 2:", part_two(input))  # 2828
