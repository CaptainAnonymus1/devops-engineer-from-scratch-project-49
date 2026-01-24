from brain_games.games_engine import engine
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

def brain_progression():
    random_list = get_random_list()
    puzzles_list = list()
    correct_answers = list()
    counter = 0

    while counter < 3:
        index = get_index()
        start_number = get_start_number(random_list, index)
        step = get_step()
        progression_list = get_progression_list(start_number, step)
        puzzle = get_puzzle(progression_list, index)
        puzzles_list.append(puzzle)
        missing_number = get_missing_number(progression_list, index)
        correct_answer = missing_number
        correct_answers.append(str(correct_answer))
        counter += 1
        
    return puzzles_list, correct_answers
    
def main():
    game_name = "brain_progression"
    task = 'What number is missing in the progression?'

    puzzles_list, correct_answers = brain_progression()
    engine(game_name, task, puzzles_list, correct_answers)
