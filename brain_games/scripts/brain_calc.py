from brain_games.games_engine import engine
from brain_games.games.calc import get_game_data


def main():
    game_name = 'brain_calculation'
    
    engine(game_name, get_game_data)
