from brain_games.games_engine import engine
from brain_games.games.progression import find


def main():
    game_name = "brain_progression"
    task = 'What number is missing in the progression?'

    puzzle, correct_answer = find()
    engine(game_name, task, puzzle, correct_answer)
