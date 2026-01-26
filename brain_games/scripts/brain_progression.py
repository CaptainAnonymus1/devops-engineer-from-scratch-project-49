from brain_games.games_engine import engine
from brain_games.games.progression import brain_progression


def main():
    game_name = "brain_progression"
    task = 'What number is missing in the progression?'

    puzzles_list, correct_answers = brain_progression()
    engine(game_name, task, puzzles_list, correct_answers)
