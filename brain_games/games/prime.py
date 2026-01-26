import random


def get_random_list():
    random_list = list()
    for _ in range(3):
        random_figure = random.randint(1, 20)
        random_list.append(random_figure)
    return random_list


def is_prime(number):
    if number < 2:
        return False
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1
    return True


def brain_prime():
    numbers = get_random_list()
    puzzles_list = list()
    correct_answers = list()
    for number in numbers:
        puzzles_list.append(number)
        correct_answer = "yes" if is_prime(number) else "no"
        correct_answers.append(str(correct_answer))
    return puzzles_list, correct_answers