import random


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
    

def find():
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)
    action = random_choice()
    puzzle = f'{first_number} {action} {second_number}'
    correct_answer = action_result(first_number, second_number, action)
    return puzzle, correct_answer
