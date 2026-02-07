from brain_games.games_engine import engine
from brain_games.games import prime


def main():
    engine(prime.get_game_data)
