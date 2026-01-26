import random


def get_random_list():
    random_list = list()
    for _ in range(6):
        random_figure = random.randint(1, 20)
        random_list.append(random_figure)
    return random_list


def brain_even():
    numbers = get_random_list()
    puzzles_list = list()
    correct_answers_list = list()
    for number in numbers:
        puzzles_list.append(str(number))
        correct_answer = "yes" if number % 2 == 0 else "no"
        correct_answers_list.append(correct_answer)
    return puzzles_list, correct_answers_list