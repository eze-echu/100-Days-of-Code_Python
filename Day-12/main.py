# Guessing Game
import random

lives = 0


def select_difficulty():
    choice = input("What difficulty do you want? (1, 2, 3)\n 1. Easy\n 2. Medium\n 3. Hard\n")
    global lives
    try:
        if int(choice) in [1, 2, 3]:
            match int(choice):
                case 1:
                    lives = 10
                case 2:
                    lives = 5
                case 3:
                    lives = 3
            return True
        else:
            return False
    except BaseException:
        return False


def guess(number: int, hidden_number: int) -> str | None:
    global lives
    if number == hidden_number:
        return "="
    elif number > hidden_number:
        lives -= 1
        return "<"
    elif number < hidden_number:
        lives -= 1
        return ">"


if __name__ == '__main__':
    print("Welcome to the Number Guessing game, you have to guess the number from 1 to 100")
    if select_difficulty():
        random_number = random.randint(1, 100)
        while True:
            if lives > 0:
                print(f"You have {lives} lives left.")
                result = guess(int(input("guess a number:\n")), random_number)
                match result:
                    case "=":
                        print(f"You've guessed the number correctly!")
                        break
                    case ">":
                        print("Too Low")
                    case "<":
                        print("Too High")
            else:
                print(f"You lost! the number was {random_number}")
                break


