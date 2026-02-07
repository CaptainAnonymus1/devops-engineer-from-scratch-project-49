from brain_games.games_engine import engine
from brain_games.games import even


def main():
    game_name = "brain-even"
    
    engine(game_name, even.get_game_data)
