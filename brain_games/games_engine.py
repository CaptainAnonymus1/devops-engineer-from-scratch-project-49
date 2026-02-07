from prompt import string


def engine(game_name, get_game_data):
    print(f"{game_name}\n")
    print("Welcome to the Brain Games!")
    user_name = string(prompt="May I have your name? ")
    print(f"Hello, {user_name}!")

    for _ in range(3):
        puzzle, correct_answer, task, game_name = get_game_data()
        print(f"{task}")
        user_answer = string(
            prompt=f'Question: {puzzle}\n')
        print(f'Your answer: {user_answer}')

        if user_answer.lower() != correct_answer:
            print(f'"{user_answer}" is wrong answer ;(. '
                 f'Correct answer was "{correct_answer}"')
            print(f"Let's try again, {user_name}!")
            break
        else:
            print("Correct!")
    else:
        print(f"Congratulations, {user_name}!")
