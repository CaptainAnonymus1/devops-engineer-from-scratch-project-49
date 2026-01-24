import random
from  brain_games.games_engine import engine

def get_random_list():
    random_list = list()
    for _ in range(6):
        random_figure = random.randint(1, 20)
        random_list.append(random_figure)
    return random_list

def random_choice():
    list_of_actions = ('+', '-', '*')
    return random.choice(list_of_actions)

def action_result(first_number, second_number, action):
    if action == '+':
        return first_number + second_number
    elif action == '-':
        return first_number - second_number
    elif action == '*':
        return first_number * second_number

def brain_calc():
    numbers = get_random_list()
    puzzles_list = list()
    correct_answers = list()
    i = 0
    counter = 0

    while counter < 3:
        first_number = numbers[i]
        second_number = numbers[i + 1]
        action = random_choice()

        puzzle = f'{first_number} {action} {second_number}'       
        puzzles_list.append(puzzle)
        correct_answer = action_result(first_number, second_number, action)
        correct_answers.append(str(correct_answer))
        counter += 1
        i += 2
    return puzzles_list, correct_answers      


def main():
    game_name = 'brain_calculation'
    task = 'What is the result of the expression?'
    
    puzzles_list, correct_answers = brain_calc()
    engine(game_name, task, puzzles_list, correct_answers)
