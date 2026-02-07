from brain_games.games_engine import engine
from brain_games.games import progression


def main():
    game_name = "brain_progression"

    engine(game_name, progression.get_game_data)
