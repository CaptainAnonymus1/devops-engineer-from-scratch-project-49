from brain_games.games_engine import engine
from brain_games.games import gcd


def main():
    engine(gcd.get_game_data)
