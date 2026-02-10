import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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
    number = random.randint(1, 20)
    correct_answer = "yes" if is_prime(number) else "no"
    puzzle = str(number)
    return puzzle, correct_answer
