from pathlib import Path

type Coord = tuple[int, int]

GRID_SIZE = 1000


def parse_line(line: str) -> tuple[str, Coord, Coord]:
    if line.startswith("turn"):
        action = line.split()[1]
        coord_1, coord_2 = line.split()[2], line.split()[4]
    else:
        action = "toggle"
        coord_1, coord_2 = line.split()[1], line.split()[3]
    x1, y1 = int(coord_1.split(",")[0]), int(coord_1.split(",")[1])
    x2, y2 = int(coord_2.split(",")[0]), int(coord_2.split(",")[1])
    return (action, (x1, y1), (x2, y2))


def get_coord_range(coord_1: Coord, coord_2: Coord) -> list[Coord]:
    x1, y1 = coord_1
    x2, y2 = coord_2
    min_x, max_x, min_y, max_y = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
    return [(x,y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1)]


def part_one():
    grid = {(x,y): 0 for x in range(0, GRID_SIZE) for y in range(0, GRID_SIZE)}
    for line in input:
        action, coord_1, coord_2 = parse_line(line)
        for x, y in get_coord_range(coord_1, coord_2):
            if action == "on":
                grid[(x,y)] = 1
            if action == "off":
                grid[(x,y)] = 0
            if action == "toggle":
                grid[(x,y)] = 1 if grid[(x,y)] == 0 else 0
    return len([state for state in grid.values() if state == 1])


def part_two():
    grid = {(x,y): 0 for x in range(0, GRID_SIZE) for y in range(0, GRID_SIZE)}
    for line in input:
        action, coord_1, coord_2 = parse_line(line)
        for x, y in get_coord_range(coord_1, coord_2):
            if action == "on":
                grid[(x,y)] += 1
            if action == "off":
                grid[(x,y)] = max(0, grid[(x,y)] - 1)
            if action == "toggle":
                grid[(x,y)] += 2
    return sum(grid.values())


if __name__ == "__main__":
    # import input
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.readlines()

    # results
    print("Part 1:", part_one()) # 569999
    print("Part 2:", part_two()) # 17836115
