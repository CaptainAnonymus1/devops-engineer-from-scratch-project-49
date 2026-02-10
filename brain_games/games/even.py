import random

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    number = random.randint(1, 20)
    correct_answer = "yes" if number % 2 == 0 else "no"
    puzzle = str(number)
    return puzzle, correct_answer