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

def is_prime(number):
    if number < 2:
        return False
    divider = 2
    while divider <= number / 2:
        if number % divider == 0:
            return False
        divider += 1
    return True


def get_correct_answer(number):
    return "yes" if is_prime(number) else "no" 


def main():
    print("brain-prime\n")
    print("Welcome to the Brain Games!")

    name = string(prompt="May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    wins_counter = 0
    puzzle = get_random_list()

    for i in range(3):
        # max 3 rounds of game required
        number = puzzle[i]
        correct_answer = get_correct_answer(number)
        
        answer = string(prompt=f"Question: {number}\n")
        print(f"Your answer: {answer}")  
        if answer != correct_answer:
            print(f'"{answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}"')
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
            wins_counter += 1

    print(f"Congratulations, {name}!")
    