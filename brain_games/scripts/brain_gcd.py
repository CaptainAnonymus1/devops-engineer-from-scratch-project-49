from brain_games.games_engine import engine
from brain_games.games.gcd import brain_gcd


def main():
    game_name = "brain_gcd"
    task = 'Find the greatest common divisor of given numbers.'

    puzzles_list, correct_answers = brain_gcd()
    engine(game_name, task, puzzles_list, correct_answers)
