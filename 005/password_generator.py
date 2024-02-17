import random
import string


def main():
    password = []

    no_of_letters = int(input("How many letters would you like in your password? "))
    no_of_digits = int(input("How many digits would you like in your password? "))
    no_of_symbols = int(input("How many symbols would you like in your password? "))

    for _ in range(no_of_letters):
        password.append(random.choice(string.ascii_letters))

    for _ in range(no_of_digits):
        password.append(random.choice(string.digits))

    for _ in range(no_of_symbols):
        password.append(random.choice("!@#$%^&()-+"))

    random.shuffle(password)

    print(f"Generated password: {''.join(password)}")


if __name__ == "__main__":
    main()
