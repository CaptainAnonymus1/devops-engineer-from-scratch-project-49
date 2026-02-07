from brain_games.games_engine import engine
from brain_games.games import prime


def main():
    game_name = "brain_prime"
 
    engine(game_name, prime.get_game_data)
