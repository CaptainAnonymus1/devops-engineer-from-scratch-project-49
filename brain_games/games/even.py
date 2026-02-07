import random


def get_game_data():
    game_name = "brain-even"
    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    number = random.randint(1, 20)
    correct_answer = "yes" if number % 2 == 0 else "no"
    puzzle = str(number)
    return puzzle, correct_answer, game_name, task
