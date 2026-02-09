import random

GAME_DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 6  # Progression task consist of 6 numbers.


def get_random_list():
    random_list = list()
    for _ in range(PROGRESSION_LENGTH):
        random_figure = random.randint(1, 20)
        # progression numbers from 1 to 20.
        random_list.append(random_figure)
    return random_list


def get_start_number(random_list):
    index = random.randint(0, 5)
    # for list of 6 numbers there are indexes from 0 to 5.
    start_number = random_list[index]
    return start_number, index


def get_step():
    step = random.randint(1, 6)
    # min step is 1, max step is 6.
    return step


def get_progression_list(start_number, step):
    progression_list = list()
    for i in range(PROGRESSION_LENGTH):
        current_number = start_number + i * step
        progression_list.append(current_number)
    return progression_list


def get_puzzle(progression_list, index):
    puzzle_list = progression_list.copy()
    puzzle_list[index] = ".."
    puzzle = ' '.join(str(x) for x in puzzle_list)
    return puzzle


def get_game_data():
    random_list = get_random_list()
    start_number, index = get_start_number(random_list)
    step = get_step()
    progression_list = get_progression_list(start_number, step)
    puzzle = get_puzzle(progression_list, index)
    correct_answer = progression_list[index]
    return puzzle, str(correct_answer)
