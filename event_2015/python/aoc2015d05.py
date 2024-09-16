import re
from pathlib import Path


def three_vowels(string):
    return len([char for char in string if char in "aeiou"]) >= 3


def repeated_chars(string):
    return any(c1 == c2 for c1, c2 in zip(string, string[1:]))


def bad_pair(string):
    return any(substring in string for substring in ["ab", "cd", "pq", "xy"])


def two_pairs(string):
    return re.search(r"(..).*\1", string) is not None


def sandwich(string):
    return re.search(r"(.).\1", string) is not None


def part_one():
    return len(
        [
            string
            for string in input
            if three_vowels(string) and repeated_chars(string) and not bad_pair(string)
        ]
    )


def part_two():
    return len([string for string in input if two_pairs(string) and sandwich(string)])


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.read().splitlines()

    print("Part 1:", part_one())  # 255
    print("Part 2:", part_two())  # 55
