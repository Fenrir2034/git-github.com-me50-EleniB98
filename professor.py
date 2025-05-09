import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = f"{x} + {y} = "
        correct_answer = x + y

        user_answer = get_user_answer(problem, correct_answer)

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", correct_answer)

    print("Your score:", score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            return level
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    return random.randint(10**(level-1), 10**level - 1)

def get_user_answer(problem, correct_answer):
    tries = 0
    while tries < 3:
        user_input = input(problem)
        try:
            user_answer = int(user_input)
            return user_answer
        except ValueError:
            print("EEE")
            tries += 1
    return correct_answer

if __name__ == "__main__":
    main()

