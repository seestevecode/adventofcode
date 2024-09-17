from pathlib import Path

KEYPAD_ONE = """\
.....
.123.
.456.
.789.
....."""

KEYPAD_TWO = """\
.......
...1...
..234..
.56789.
..ABC..
...D...
......."""


def find_in_nested_list(grid, entry):
    for line in grid:
        if entry in line:
            return grid.index(line), line.index(entry)
    raise ValueError("Not found in nested list")


def move(keypad, start_entry, direction):
    keypad_list = keypad.strip("\n").split("\n")
    start_row, start_col = find_in_nested_list(keypad_list, start_entry)
    match direction:
        case "U":
            new_row, new_col = start_row - 1, start_col
        case "R":
            new_row, new_col = start_row, start_col + 1
        case "D":
            new_row, new_col = start_row + 1, start_col
        case "L":
            new_row, new_col = start_row, start_col - 1
        case _:
            new_row, new_col = start_row, start_col
    return (
        start_entry
        if keypad_list[new_row][new_col] == "."
        else keypad_list[new_row][new_col]
    )


def solve(keypad):
    entry, code = "5", []
    for line in input:
        for direction in line:
            entry = move(keypad, entry, direction)
        code.append(entry)
    return "".join(map(str, code))


def part_one():
    return solve(KEYPAD_ONE)


def part_two():
    return solve(KEYPAD_TWO)


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.read().strip("\n").split("\n")

    print("Part 1:", part_one())  # 52981
    print("Part 2:", part_two())  # 74CD2
