from pathlib import Path
import hashlib


def hex_from_hash(hash_string: str) -> str:
    md5_hash = hashlib.md5()
    md5_hash.update(hash_string.encode("utf-8"))
    return md5_hash.hexdigest()


def solve() -> tuple[str, str]:
    counter = 0
    password_one, password_two = [], ["*"] * 8
    while len(password_one) < 8 or password_two.count("*"):
        hex = hex_from_hash(input.strip("\n") + str(counter))
        if hex.startswith("00000"):
            if len(password_one) < 8:
                password_one.append(hex[5])
            if hex[5] in "01234567" and password_two[int(hex[5])] == "*":
                password_two[int(hex[5])] = hex[6]
        counter += 1
    return "".join(password_one), "".join(password_two)


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.read()

    part_one, part_two = solve()

    print("Part 1:", part_one)  # d4cd2ee1
    print("Part 2:", part_two)  # f2c730e5
