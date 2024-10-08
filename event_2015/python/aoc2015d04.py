import hashlib


def find_lowest_num(start_string):
    num = 1
    while (
        not hashlib.md5((input + str(num)).encode())
        .hexdigest()
        .startswith(start_string)
    ):
        num += 1
    return num


def part_one():
    return find_lowest_num("00000")


def part_two():
    return find_lowest_num("000000")


if __name__ == "__main__":
    input = "ckczppom"

    print("Part 1:", part_one())  # 117946
    print("Part 2:", part_two())  # 3938038
