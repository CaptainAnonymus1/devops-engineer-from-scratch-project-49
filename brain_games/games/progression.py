import random

RULES = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 6  # Progression task consist of 6 numbers.


def get_progression_list():
    start_number = random.randint(1, 20)
    # min start number is 1, max start number is 20.
    step = random.randint(1, 6)
    # min step is 1, max step is 6.   
    progression_list = list()
    for i in range(PROGRESSION_LENGTH):
        current_number = start_number + i * step
        progression_list.append(current_number)
    return progression_list


def get_game_data():
    progression_list = get_progression_list()
    puzzle_list = progression_list.copy()
    index = random.randint(0, 5)
    # for progression list of 6 numbers there are indexes from 0 to 5.
    correct_answer = progression_list[index]
    puzzle_list[index] = ".."
    puzzle = ' '.join(str(x) for x in puzzle_list)
    return puzzle, str(correct_answer)
