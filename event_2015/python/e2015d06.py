from pathlib import Path

type Coord = tuple[int, int]

GRID_SIZE = 1000
INITIAL_GRID = {(x,y): 0 for x in range(0, GRID_SIZE) for y in range(0, GRID_SIZE)}
ACTIONS = {
    (1, "on"): lambda _: 1, (1, "off"): lambda _: 0, (1, "toggle"): lambda x: 1 if x == 0 else 0,
    (2, "on"): lambda x: x + 1, (2, "off"): lambda x: max(0, x - 1), (2, "toggle"): lambda x: x + 2
}


def parse_line(line: str) -> tuple[str, Coord, Coord]:
    if line.startswith("turn"):
        _, action, coord_1, _, coord_2 = line.split()
    else:
        assert line.startswith("toggle")
        action, coord_1, _, coord_2 = line.split()
    x1, y1 = map(int, coord_1.split(","))
    x2, y2 = map(int, coord_2.split(","))
    return (action, (x1, y1), (x2, y2))


def get_coord_range(coord_1: Coord, coord_2: Coord) -> list[Coord]:
    x1, y1 = coord_1
    x2, y2 = coord_2
    min_x, max_x, min_y, max_y = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
    return [(x, y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1)]


def part(part_number: int) -> int:
    grid = INITIAL_GRID.copy()
    for line in input:
        action, coord_1, coord_2 = parse_line(line)
        for x, y in get_coord_range(coord_1, coord_2):
             grid[(x, y)] = (ACTIONS[(part_number, action)])(grid[(x, y)])
    return sum(grid.values())

if __name__ == "__main__":
    # import input
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = f.readlines()

    # results
    print("Part 1:", part(1)) # 569999
    print("Part 2:", part(2)) # 17836115
