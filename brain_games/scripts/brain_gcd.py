from brain_games.games_engine import engine
from brain_games.games.gcd import get_game_data


def main():
    game_name = "brain_gcd"
    
    engine(game_name, get_game_data)
