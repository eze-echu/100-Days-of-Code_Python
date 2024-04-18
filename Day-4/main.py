import ascii_art
import random

if __name__ == '__main__':
    choices = [ascii_art.rock, ascii_art.paper, ascii_art.scissors]
    print("WELCOME TO ROCK PAPER SCISSORS: PYTHON EDITION\n"
          "SELECT 0 FOR ROCK, 1 FOR PAPER, 2 FOR SCISSORS\n")
    while True:
        try:
            input_choice = input()
            if int(input_choice) in range(0, 2):
                break
            else:
                raise ValueError
        except TypeError:
            print("INVALID INPUT")
        except ValueError:
            print("INVALID INPUT")
    input_choice = int(input_choice)
    computer_choice = random.randint(0, 2)
    print("You: \n" + choices[input_choice])
    print("computer:\n" + choices[computer_choice])
    if input_choice == computer_choice:
        print("TIE")
    elif input_choice == 0:
        if computer_choice == 1:
            print("YOU LOSE")
        else:
            print("YOU WIN")
    elif input_choice == 1:
        if computer_choice == 2:
            print("YOU LOSE")
        else:
            print("YOU WIN")
    else:
        if computer_choice == 0:
            print("YOU LOSE")
        else:
            print("YOU WIN")
