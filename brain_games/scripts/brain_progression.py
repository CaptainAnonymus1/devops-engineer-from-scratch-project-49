import random

from prompt import string

# generator
# list of 6 random numbers = max 3 rounds of game required.


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
    puzzle_list[index] = "..."
    puzzle = ' '.join(str(x) for x in puzzle_list)
    return puzzle


def main():
    print("brain-progression\n")
    print("Welcome to the Brain Games!")
    name = string(prompt="May I have your name? ")
    print(f"Hello, {name}!")
    print('What number is missing in the progression?')

    wins_counter = 0
    
    while wins_counter < 3:
        random_list = get_random_list()
        index = get_index()
        start_number = get_start_number(random_list, index)
        step = get_step()
        progression_list = get_progression_list(start_number, step)
        puzzle = get_puzzle(progression_list, index)
        missing_number = get_missing_number(progression_list, index)
        correct_answer = missing_number

        answer = string(
            prompt=f"Question: {puzzle}\n"
        )
        print(f"Your answer: {answer}")
        if int(answer) != correct_answer:
            print(f'{answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}')
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
            wins_counter += 1
    print(f"Congratulations, {name}!")