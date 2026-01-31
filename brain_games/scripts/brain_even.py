from brain_games.games_engine import engine
from brain_games.games.even import find


def main():
    game_name = "brain-even"
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    
    puzzle, correct_answer = find()
    engine(game_name, task, puzzle, correct_answer)
