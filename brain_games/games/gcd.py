import random


def get_random_list():
    random_list = list()
    for _ in range(6):
        random_figure = random.randint(1, 20)
        random_list.append(random_figure)
    return random_list


def get_gcd(first_number, second_number):
    a = first_number
    b = second_number
    while b != 0:
        c = a % b
        a = b
        b = c
    gcd = a
    return gcd


def find():
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)
    puzzle = f'{first_number} {second_number}'
    correct_answer = get_gcd(first_number, second_number)
    return puzzle, str(correct_answer)
