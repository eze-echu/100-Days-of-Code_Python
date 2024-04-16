import os
import colorama

if __name__ == "__main__":
    try:
        print("Insert Day Number:")
        day = int(input("> "))
        if day < 1:
            raise ValueError
        if not os.path.isdir(os.path.join(os.getcwd(), f"Day-{day}")):
            os.makedirs(os.path.join(os.getcwd(), f"Day-{day}"), exist_ok=False)
            with open(os.path.join(os.getcwd(), f"Day-{day}/Sandbox.ipynb"), "w") as file:
                pass
            with open(os.path.join(os.getcwd(), f"Day-{day}/main.py"), "w") as file:
                pass

        else:
            raise FileExistsError
    except TypeError:
        print(colorama.Fore.RED, "Invalid input, make sure you insert an integer")
    except ValueError:
        print(colorama.Fore.RED, "Invalid input, input must be an integer greater than 0")
    except FileExistsError:
        print(colorama.Fore.YELLOW, "Error: File/Folder already exists")
