from pathlib import Path

# import input
event_dir = Path(__file__).parents[1]
file_name = Path(__file__).stem
with open(event_dir / "inputs" / file_name) as f:
    input = f.read()


def move(x, y, direction):
    match direction:
        case "^":
            y += 1
        case ">":
            x += 1
        case "v":
            y -= 1
        case "<":
            x -= 1
    return x, y


# part 1
def part_one():
    x_coord = y_coord = 0
    visited_coords = {(0, 0)}
    for direction in input:
        x_coord, y_coord = move(x_coord, y_coord, direction)
        visited_coords.add((x_coord, y_coord))
    return len(visited_coords)


# part 2
def part_two():
    direction_pairs = [(input[i], input[i + 1]) for i in range(0, len(input) - 1, 2)]
    santa_x = santa_y = robo_x = robo_y = 0
    visited_coords = {(0, 0)}
    for santa_dir, robo_dir in direction_pairs:
        santa_x, santa_y = move(santa_x, santa_y, santa_dir)
        robo_x, robo_y = move(robo_x, robo_y, robo_dir)
        visited_coords.add((santa_x, santa_y))
        visited_coords.add((robo_x, robo_y))
    return len(visited_coords)


# results
print("Part 1:", part_one())  # 2081
print("Part 2:", part_two())  # 2341
