import random


def find():
    number = random.randint(1, 20)
    correct_answer = "yes" if number % 2 == 0 else "no"
    puzzle = str(number)
    return puzzle, correct_answer
