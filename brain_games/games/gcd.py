import random


def get_gcd(first_number, second_number):
    a = first_number
    b = second_number
    while b != 0:
        c = a % b
        a = b
        b = c
    gcd = a
    return gcd


def get_game_data():
    game_name = "brain-gcd"
    game_task = 'Find the greatest common divisor of given numbers.'
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)
    puzzle = f'{first_number} {second_number}'
    correct_answer = get_gcd(first_number, second_number)
    return puzzle, str(correct_answer), game_task, game_name
