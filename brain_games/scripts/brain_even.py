from brain_games.games_engine import engine
from brain_games.games.even import get_game_data


def main():
    game_name = "brain-even"
        
    engine(game_name, get_game_data)
