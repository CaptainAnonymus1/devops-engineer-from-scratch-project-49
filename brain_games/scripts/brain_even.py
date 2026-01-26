from brain_games.games_engine import engine
from brain_games.games.even import brain_even


def main():
    game_name = "brain-even"
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    
    puzzles_list, correct_answers = brain_even()
    engine(game_name, task, puzzles_list, correct_answers)
