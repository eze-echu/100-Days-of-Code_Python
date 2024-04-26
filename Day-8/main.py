alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(text: str, key: int) -> str | BaseException:
    encoded_text = ""
    try:
        for letter in text.lower():
            if letter in alphabet:
                value = alphabet.index(letter) + key
                if value >= len(alphabet):
                    value -= len(alphabet)
                encoded_text += alphabet[value]
            else:
                encoded_text += letter
    except ValueError:
        return ValueError()
    return encoded_text


def decrypt(text: str, key: int) -> str | BaseException:
    decoded_text = ""
    try:
        for letter in text.lower():
            if letter in alphabet:
                value = alphabet.index(letter) - key
                if value <= len(alphabet) * -1:
                    value += alphabet
                decoded_text += alphabet[value]
            else:
                decoded_text += letter
    except ValueError:
        return ValueError()
    return decoded_text


def menu():
    choice = input("Caesar Cypher"
                   "\n1. Encrypt"
                   "\n2. Decrypt\n")
    if choice.lower() in ["1", "encrypt", "2", "decrypt"]:
        match choice.lower():
            case "1" | "encrypt":
                text = input("Enter message\n")
                key = input("Enter key \n")
                if key.isnumeric():
                    print(f"Your secret message is: {encrypt(text, int(key) % len(alphabet))}")
                else:
                    raise TypeError()

            case "2" | "decrypt":
                text = input("Enter message\n")
                key = input("Enter key \n")
                if key.isnumeric():
                    print(f"Your message is: {decrypt(text, int(key) % len(alphabet))}")
                else:
                    raise TypeError()
    else:
        raise ValueError("Please input either a number or an option")

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g.
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
#https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.


if __name__ == "__main__":
    while True:
        try:
            menu()
        except ValueError:
            print("Please input a proper value")
            continue
        except TypeError:
            print("Type error, check your input")
            continue
