from pathlib import Path

DIRECTIONS = ["N", "E", "S", "W"]


def turn(facing, turn_direction):
    facing_index = DIRECTIONS.index(facing)
    if turn_direction == "R":
        return DIRECTIONS[(facing_index + 1) % len(DIRECTIONS)]
    else:
        assert turn_direction == "L"
        return DIRECTIONS[(facing_index - 1) % len(DIRECTIONS)]


def move(facing, start_x, start_y, distance):
    match facing:
        case "N":
            return start_x, start_y + distance
        case "E":
            return start_x + distance, start_y
        case "S":
            return start_x, start_y - distance
        case "W":
            return start_x - distance, start_y
        case _:
            return start_x, start_y


def part_one():
    facing, coord_x, coord_y = "N", 0, 0
    for instruction in input:
        facing = turn(facing, instruction[0])
        coord_x, coord_y = move(facing, coord_x, coord_y, int(instruction[1:]))
    return abs(coord_x) + abs(coord_y)


def part_two():
    facing, coord_x, coord_y = "N", 0, 0
    visited = [(coord_x, coord_y)]
    for instruction in input:
        facing = turn(facing, instruction[0])
        for _ in range(int(instruction[1:])):
            coord_x, coord_y = move(facing, coord_x, coord_y, 1)
            if (coord_x, coord_y) in visited:
                return abs(coord_x) + abs(coord_y)
            else:
                visited.append((coord_x, coord_y))
    return "No solution found"


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.read().strip("\n").split(", ")

    print("Part 1:", part_one())  # 353
    print("Part 2:", part_two())  # 152
