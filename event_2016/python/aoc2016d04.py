from collections import Counter
from pathlib import Path

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def parse_row(row: str) -> tuple[str, int, str]:
    last_dash, first_bracket = row.rfind("-"), row.find("[")
    encrypted_name = row[:last_dash]
    sector_id = int(row[last_dash + 1 : first_bracket])
    checksum = row[first_bracket + 1 : row.find("]")]
    return encrypted_name, sector_id, checksum


def is_valid_sector(encrypted_name: str, checksum: str) -> bool:
    most_common = Counter(encrypted_name.replace("-", "")).most_common()
    most_common_sorted = sorted(most_common, key=lambda x: (-x[1], x[0]))
    return "".join(list(map(lambda x: x[0], most_common_sorted[:5]))) == checksum


def rotate_cipher(encrypted_name: str, sector_id: int) -> str:
    return "".join(
        [
            (
                ALPHABET[(ALPHABET.index(encrypted_name[idx]) + sector_id) % 26]
                if encrypted_name[idx] != "-"
                else " "
            )
            for idx in range(len(encrypted_name))
        ]
    )


def part_one() -> int:
    return sum([row[1] for row in parsed_input if is_valid_sector(row[0], row[2])])


def part_two() -> int:
    for row in parsed_input:
        encrypted_name, sector_id, _ = row
        if rotate_cipher(encrypted_name, sector_id) == "northpole object storage":
            return sector_id
    return -1


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.readlines()

    parsed_input = [parse_row(row) for row in input]

    print("Part 1:", part_one())  # 361724
    print("Part 2:", part_two())  # 482
