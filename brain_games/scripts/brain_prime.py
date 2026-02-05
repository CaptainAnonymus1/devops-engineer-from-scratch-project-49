from brain_games.games_engine import engine
from brain_games.games.prime import get_game_data


def main():
    game_name = "brain_prime"
 
    engine(game_name, get_game_data)
