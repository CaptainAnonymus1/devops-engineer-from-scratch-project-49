from brain_games.games_engine import engine
from brain_games.games import progression


def main():
    engine(progression.get_game_data)
