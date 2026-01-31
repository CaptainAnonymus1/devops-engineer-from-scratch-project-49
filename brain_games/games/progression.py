import random


def get_random_list():
    random_list = list()
    for _ in range(6):
        random_figure = random.randint(1, 20)
        random_list.append(random_figure)
    return random_list


def get_index():
    index = random.randint(0, 5)
    return index


def get_start_number(random_list, index):
    start_number = random_list[index]
    return start_number


def get_step():
    step = random.randint(1, 6)
    return step


def get_progression_list(start_number, step):
    progression_list = list()
    for i in range(6):
        current_number = start_number + i * step
        progression_list.append(current_number)
    return progression_list


def get_missing_number(progression_list, index):
    missing_number = progression_list[index]
    return missing_number


def get_puzzle(progression_list, index):
    puzzle_list = progression_list.copy()
    puzzle_list[index] = ".."
    puzzle = ' '.join(str(x) for x in puzzle_list)
    return puzzle


def find():
    random_list = get_random_list()
    index = get_index()
    start_number = get_start_number(random_list, index)
    step = get_step()
    progression_list = get_progression_list(start_number, step)
    puzzle = get_puzzle(progression_list, index)
    missing_number = get_missing_number(progression_list, index)
    correct_answer = str(missing_number)
    return puzzle, correct_answer
