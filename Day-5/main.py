#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


def easy_gen(letter_quantity, symbol_quantity, number_quantity) -> str:
    password = ""
    for i in range(letter_quantity):
        password += random.choice(letters)
    for i in range(symbol_quantity):
        password += random.choice(symbols)
    for i in range(number_quantity):
        password += random.choice(numbers)
    return password

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
def hard_gen(letter_quantity, symbol_quantity, number_quantity) -> str:
    password = ""
    count = 0
    while letter_quantity + symbol_quantity + number_quantity > 0:
        count += 1
        next_type = random.randint(0, 2)
        if next_type == 0:
            if letter_quantity != 0:
                password += random.choice(letters)
                letter_quantity -= 1
            else:
                continue
        elif next_type == 1:
            if symbol_quantity != 0:
                password += random.choice(symbols)
                symbol_quantity -= 1
            else:
                continue
        elif next_type == 2:
            if number_quantity != 0:
                password += random.choice(numbers)
                number_quantity -= 1
            else:
                continue
    print(count)
    return password


def proper_hard_gen(letter_quantity, symbol_quantity, number_quantity) -> str:
    password_list = []
    count = 0

    for char in range(1, nr_letters + 1):
        count += 1
        password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
        count += 1
        password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
        count += 1
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    return password


print(f"Easy generator: {easy_gen(nr_letters, nr_symbols, nr_numbers)}")
print(f"Hard generator: {hard_gen(nr_letters, nr_symbols, nr_numbers)}")
print(f"Proper generator: {proper_hard_gen(nr_letters, nr_symbols, nr_numbers)}")
