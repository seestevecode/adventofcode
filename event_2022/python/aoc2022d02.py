from pathlib import Path

SHAPE = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
OUTCOME = {"X": "Loss", "Y": "Draw", "Z": "Win"}
OUTCOME_POINTS = {"Loss": 0, "Draw": 3, "Win": 6}
CHOICE_POINTS = {"Rock": 1, "Paper": 2, "Scissors": 3}
WINNING_GAMES = [("Rock", "Paper"), ("Paper", "Scissors"), ("Scissors", "Rock")]


def part_one(input):
    total_score = 0
    for raw_row in input:
        them, us = SHAPE[raw_row[0]], SHAPE[raw_row[1]]
        outcome = (
            "Win" if (them, us) in WINNING_GAMES else "Draw" if them == us else "Loss"
        )
        total_score += OUTCOME_POINTS[outcome] + CHOICE_POINTS[us]
    return total_score


def part_two(input):
    total_score = 0
    for raw_row in input:
        them, outcome = SHAPE[raw_row[0]], OUTCOME[raw_row[1]]
        us = (
            [win[1] for win in WINNING_GAMES if them == win[0]][0]
            if outcome == "Win"
            else [win[0] for win in WINNING_GAMES if them == win[1]][0]
            if outcome == "Loss"
            else them
        )
        total_score += OUTCOME_POINTS[outcome] + CHOICE_POINTS[us]
    return total_score


if __name__ == "__main__":
    event_dir = Path(__file__).parents[1]
    file_name = Path(__file__).stem
    with open(event_dir / "inputs" / file_name) as f:
        input = list(map(lambda x: tuple(x.split()), f.read().strip().split("\n")))

    print("Part 1:", part_one(input))  # 11603
    print("Part 2:", part_two(input))  # 12725
