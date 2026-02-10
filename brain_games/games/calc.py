import random

RULES = 'What is the result of the expression?'


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
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)
    action = random_choice()
    puzzle = f'{first_number} {action} {second_number}'
    correct_answer = str(action_result(first_number, second_number, action))
    return puzzle, correct_answer
