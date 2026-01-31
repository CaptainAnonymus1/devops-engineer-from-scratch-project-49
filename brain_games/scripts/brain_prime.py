from brain_games.games_engine import engine
from brain_games.games.prime import find


def main():
    game_name = "brain_prime"
    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'

    engine(game_name, task, find)
