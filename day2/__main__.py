from utils import load_data


class RockPaperScissors:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def part1(opponent_encoded, recommended_encoded):
    if opponent_encoded == "A":
        opponent = RockPaperScissors.ROCK
    elif opponent_encoded == "B":
        opponent = RockPaperScissors.PAPER
    elif opponent_encoded == "C":
        opponent = RockPaperScissors.SCISSORS
    
    if recommended_encoded == "X":
        recommended = RockPaperScissors.ROCK
    elif recommended_encoded == "Y":
        recommended = RockPaperScissors.PAPER
    elif recommended_encoded == "Z":
        recommended = RockPaperScissors.SCISSORS
    
    return opponent, recommended


def part2(opponent_encoded, recommended_encoded):
    if opponent_encoded == "A":
        opponent = RockPaperScissors.ROCK
    elif opponent_encoded == "B":
        opponent = RockPaperScissors.PAPER
    elif opponent_encoded == "C":
        opponent = RockPaperScissors.SCISSORS
    
    if recommended_encoded == "X":
        recommended = RockPaperScissors.ROCK if opponent == RockPaperScissors.PAPER else RockPaperScissors.PAPER if opponent == RockPaperScissors.SCISSORS else RockPaperScissors.SCISSORS
    elif recommended_encoded == "Y":
        recommended = opponent
    elif recommended_encoded == "Z":
        recommended = RockPaperScissors.ROCK if opponent == RockPaperScissors.SCISSORS else RockPaperScissors.PAPER if opponent == RockPaperScissors.ROCK else RockPaperScissors.SCISSORS
    
    return opponent, recommended


def round_score(opponent, recommended):
    outcome = 0
    if opponent == recommended:
        outcome = 3
    if (opponent == RockPaperScissors.ROCK and recommended == RockPaperScissors.PAPER) or \
        (opponent == RockPaperScissors.PAPER and recommended == RockPaperScissors.SCISSORS) or \
        (opponent == RockPaperScissors.SCISSORS and recommended == RockPaperScissors.ROCK):
        outcome = 6
    total_round_result = outcome + (1 if recommended == RockPaperScissors.ROCK else 0) + (2 if recommended == RockPaperScissors.PAPER else 0) + (3 if recommended == RockPaperScissors.SCISSORS else 0)
    return total_round_result

if __name__ == "__main__":
    # load data.
    data = load_data("./day2/data")
    
    total_score_part1 = 0
    for match in data:
        opponent_encoded, _, recommended_encoded = match.partition(" ")

        opponent, recommended = part1(opponent_encoded, recommended_encoded)
        total_score_part1 += round_score(opponent, recommended)

    print(f"Part One, Total score: {total_score_part1}")

    total_score_part2 = 0
    for match in data:
        opponent_encoded, _, recommended_encoded = match.partition(" ")

        opponent, recommended = part2(opponent_encoded, recommended_encoded)
        total_score_part2 += round_score(opponent, recommended)
    
    print(f"Part Two, Total Score: {total_score_part2}")