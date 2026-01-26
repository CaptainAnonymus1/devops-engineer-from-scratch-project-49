import random
from brain_games.games_engine import engine
from brain_games.games.calc import get_random_list, random_choice, action_result, brain_calc


def main():
    game_name = 'brain_calculation'
    task = 'What is the result of the expression?'
    
    puzzles_list, correct_answers = brain_calc()
    engine(game_name, task, puzzles_list, correct_answers)
