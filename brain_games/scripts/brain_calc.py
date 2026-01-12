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


def random_choice():
    list_of_actions = ('+', '-', '*')
    return random.choice(list_of_actions)


def action_result(first_number, second_number, action):
    if action == '+':
        return first_number + second_number
    elif action == '-':
        return first_number - second_number
    elif action == '*':
        return first_number * second_number


def main():
    print("brain-calc\n")
    print("Welcome to the Brain Games!")
    name = string(prompt="May I have your name? ")
    print(f"Hello, {name}!")
    print('What is the result of the expression?')

    list_of_numbers = get_random_list()
    i = 0
    wins_counter = 0

    while wins_counter <= 3 and (i + 1) < len(list_of_numbers):
        # max 3 rounds of game required
        first_number = list_of_numbers[i]
        second_number = list_of_numbers[i + 1]
        action = random_choice()
        correct_answer = action_result(first_number, second_number, action)
        answer = string(
            prompt=f"Question: {first_number} {action} {second_number}\n"
        )
        print(f"Your answer: {answer}")
        
        if int(answer) != correct_answer:
            print(f'{answer} is wrong answer ;(. '
                  f' Correct answer was {correct_answer}')
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
            wins_counter += 1
            i += 2

    print(f"Congratulations, {name}!")
