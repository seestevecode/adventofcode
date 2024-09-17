from pathlib import Path


def valid_candidate(candidate):
    side_1, side_2, side_3 = candidate
    return (
        side_1 + side_2 > side_3
        and side_2 + side_3 > side_1
        and side_3 + side_1 > side_2
    )


def count_candidates(array):
    return len([candidate for candidate in array if valid_candidate(candidate)])


def part_one():
    return count_candidates(input)


def part_two():
    chunk_threes = lambda lst: [lst[i : i + 3] for i in range(0, len(lst), 3)]
    transposed_input = [list(zip(*inner)) for inner in chunk_threes(input)]
    flattened_input = [item for sublist in transposed_input for item in sublist]
    return count_candidates(flattened_input)


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        raw_input = f.read().strip("\n").split("\n")

    input = [list(map(int, row.split())) for row in raw_input]

    print("Part 1:", part_one())  # 917
    print("Part 2:", part_two())  # 1649
