from brain_games.games_engine import engine
from brain_games.games.calc import find


def main():
    game_name = 'brain_calculation'
    task = 'What is the result of the expression?'
    
    puzzle, correct_answer = find()
    engine(game_name, task, puzzle, correct_answer)
