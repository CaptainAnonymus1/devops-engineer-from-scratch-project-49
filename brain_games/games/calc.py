import random


def random_choice():
    list_of_actions = ('+', '-', '*')
    return random.choice(list_of_actions)


def action_result(first_number, second_number, action):
    match action:
        case '+':
            return first_number + second_number
        case '-':
            return first_number - second_number
        case '*':
            return first_number * second_number
    

def get_game_data():
    game_name = 'brain_calculation'
    task = 'What is the result of the expression?'
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)
    action = random_choice()
    puzzle = f'{first_number} {action} {second_number}'
    correct_answer = str(action_result(first_number, second_number, action))
    return puzzle, correct_answer, task, game_name
