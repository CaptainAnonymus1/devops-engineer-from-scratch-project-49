from brain_games.games_engine import engine
from brain_games.games.gcd import find


def main():
    game_name = "brain_gcd"
    task = 'Find the greatest common divisor of given numbers.'

    engine(game_name, task, find)
