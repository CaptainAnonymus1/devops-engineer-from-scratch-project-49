from prompt import string


def engine(game_name, task, find):
    print(f"{game_name}\n")
    print("Welcome to the Brain Games!")
    user_name = string(prompt="May I have your name? ")
    print(f"Hello, {user_name}!")
    print(f"{task}")

    wins_counter = 0
    i = 0
    while wins_counter < 3:
        puzzle, correct_answer = find()

        user_answer = string(
            prompt=f'Question: {puzzle}\n')
        print(f'Your answer: {user_answer}')

        if user_answer != correct_answer:
            print(f'"{user_answer}" is wrong answer ;(. '
                 f'Correct answer was "{correct_answer}"')
            print(f"Let's try again, {user_name}!")
            return
        else:
            print("Correct!")
            wins_counter += 1
            i += 1

    print(f"Congratulations, {user_name}!")
