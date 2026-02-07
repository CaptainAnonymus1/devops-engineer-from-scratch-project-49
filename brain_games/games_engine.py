from prompt import string


def engine(get_game_data):
    print("Welcome to the Brain Games!")
    user_name = string(prompt="May I have your name? ")
    print(f"Hello, {user_name}!")
    game_task = get_game_data()[2]
    print(f"{game_task}")

    for _ in range(3):
        result = get_game_data()
        puzzle = result[0]
        correct_answer = result[1]
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
