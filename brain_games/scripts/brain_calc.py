from brain_games.games_engine import engine
from brain_games.games import calc


def main(): 
    game_name = "brain-calc"

    engine(game_name, calc.get_game_data)
    