import random


def is_prime(number):
    if number < 2:
        return False
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1
    return True


def get_game_data():
    game_name = "brain-prime"
    game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    number = random.randint(1, 20)
    correct_answer = "yes" if is_prime(number) else "no"
    puzzle = str(number)
    return puzzle, correct_answer, game_task, game_name
