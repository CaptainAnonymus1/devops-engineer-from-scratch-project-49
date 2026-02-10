from prompt import string

ROUNDS_COUNT = 3
# Maximum 3 rounds required to win the game.


def start_game(game_module):
    print("Welcome to the Brain Games!")
    user_name = string(prompt="May I have your name? ")
    print(f"Hello, {user_name}!")
    game_task = game_module.RULES
    print(f"{game_task}")

    for _ in range(ROUNDS_COUNT):
        puzzle, correct_answer = game_module.get_game_data()
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
