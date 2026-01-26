from brain_games.games_engine import engine
from brain_games.games.progression import get_random_list, get_index, brain_progression, get_start_number, get_step, get_progression_list, get_missing_number, get_puzzle
import random


def main():
    game_name = "brain_progression"
    task = 'What number is missing in the progression?'

    puzzles_list, correct_answers = brain_progression()
    engine(game_name, task, puzzles_list, correct_answers)
