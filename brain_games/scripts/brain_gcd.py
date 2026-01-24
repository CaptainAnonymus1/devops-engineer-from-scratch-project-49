from brain_games.games_engine import engine
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

def brain_gcd():
    numbers = get_random_list()
    puzzles_list = list()
    correct_answers = list()
    i = 0
    counter = 0

    while counter < 3:
        first_number = numbers[i]
        second_number = numbers[i + 1]
        puzzle = f'{first_number} {second_number}'       
        puzzles_list.append(puzzle)
        correct_answer = get_gcd(first_number, second_number)
        correct_answers.append(str(correct_answer))
        counter += 1
        i += 2
    return puzzles_list, correct_answers 

def main():
    game_name = "brain_gcd"
    task = 'Find the greatest common divisor of given numbers.'

    puzzles_list, correct_answers = brain_gcd()
    engine(game_name, task, puzzles_list, correct_answers)
