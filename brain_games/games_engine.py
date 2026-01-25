from prompt import string


def engine(game_name, task, puzzles_list, correct_answers):
    print(f"{game_name}\n")
    print("Welcome to the Brain Games!")
    user_name = string(prompt="May I have your name? ")
    print(f"Hello, {user_name}!")
    print(f"{task}")

    wins_counter = 0
    i = 0
    while wins_counter < 3:
        current_puzzle = puzzles_list[i]
        current_correct_answer = correct_answers[i]

        user_answer = string(
            prompt=f'Question: {current_puzzle}\n')
        print(f'Your answer: {user_answer}')

        if user_answer != current_correct_answer:
            print(f'"{user_answer}" is wrong answer ;(. '
                 f'Correct answer was "{current_correct_answer}"')
            print(f"Let's try again, {user_name}!")
            return
        else:
            print("Correct!")
            wins_counter += 1
            i += 1

    print(f"Congratulations, {user_name}!")
