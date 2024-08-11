from pathlib import Path

# import input
event_dir = Path(__file__).parents[1]
file_name = Path(__file__).stem
with open(event_dir / "inputs" / file_name) as f:
    input = f.read()


# part 1
def part_one():
    return input.count("(") - input.count(")")


# part 2
def part_two():
    level = 0
    for idx, char in enumerate(input):
        level = level - 1 if char == ")" else level + 1
        if level == -1:
            return idx + 1


# results
print("Part 1:", part_one())  # 280
print("Part 2:", part_two())  # 1917
