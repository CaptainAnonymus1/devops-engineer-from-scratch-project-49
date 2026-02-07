from brain_games.games_engine import engine
from brain_games.games import even


def main():
    engine(even.get_game_data)
