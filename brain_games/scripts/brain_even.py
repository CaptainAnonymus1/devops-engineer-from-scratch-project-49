#!/usr/bin/env python3

import random
from prompt import string

# generator 
# list of 3 random numbers = max 3 rounds of game required.


def get_random_list():
    random_list = list()
    for _ in range(3):
        random_figure = random.randint(1, 99)
        random_list.append(random_figure)
    return random_list


# validator

def is_even(number):
    return number % 2 == 0


def main():
    print("brain-even\n")
    print("Welcome to the Brain Games!")

    name = string(prompt="May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    puzzle = get_random_list()
    wins_counter = 0
    for i in range(3):
        # max 3 rounds of game required
        number = puzzle[i]
        answer = string(prompt=f"Question: {number}\n")
        print(f"Your answer: {answer}!")
        correct_answer = "yes" if is_even(number) else "no"    
        if answer != correct_answer:
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}')
            print(f"Let's try again, {name}")
            return
        else:
            print("Correct!")
            wins_counter += 1

    print(f"Congratulations, {name}!")
    