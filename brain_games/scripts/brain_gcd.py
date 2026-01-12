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


def get_gcd(first_number, second_number):
    a = first_number
    b = second_number
    while b != 0:
        c = a % b
        a = b
        b = c
    gcd = a
    return gcd


def main():
    print("brain-gsd\n")
    print("Welcome to the Brain Games!")
    name = string(prompt="May I have your name? ")
    print(f"Hello, {name}!")
    print('Find the greatest common divisor of given numbers.')

    list_of_numbers = get_random_list()
    i = 0
    wins_counter = 0
    while wins_counter <= 3 and (i + 1) < len(list_of_numbers):
        # max 3 rounds of game required
        first_number = list_of_numbers[i]
        second_number = list_of_numbers[i + 1]  
        correct_answer = get_gcd(first_number, second_number)
        answer = string(
            prompt=f"Question: {first_number}, {second_number}\n"
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
            i += 2
    print(f"Congratulations, {name}!")
