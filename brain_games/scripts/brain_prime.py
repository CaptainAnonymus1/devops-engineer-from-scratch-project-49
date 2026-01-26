from brain_games.games_engine import engine
from brain_games.games.prime import get_random_list, is_prime, brain_prime
import random


def main():
    game_name = "brain_prime"
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    puzzles_list, correct_answers = brain_prime()
    engine(game_name, task, puzzles_list, correct_answers)
