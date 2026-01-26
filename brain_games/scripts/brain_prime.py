from brain_games.games_engine import engine
from brain_games.games.prime import brain_prime


def main():
    game_name = "brain_prime"
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    puzzles_list, correct_answers = brain_prime()
    engine(game_name, task, puzzles_list, correct_answers)
