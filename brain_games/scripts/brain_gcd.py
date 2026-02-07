from brain_games.games_engine import engine
from brain_games.games import gcd


def main():
    game_name = "brain_gcd"
    
    engine(game_name, gcd.get_game_data)
