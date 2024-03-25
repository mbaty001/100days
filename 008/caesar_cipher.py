"""
Encode given word using Ceasar Cipher
"""

from string import ascii_lowercase


def main():
    """Entrypoint"""

    while True:
        action = ""
        message = ""
        shift = -1
        once_more = ""

        while action not in ["decode", "encode"]:
            action = input(
                "Type 'encode' to encrypt , type 'decode' to decrypt: "
            ).lower()

        while len(message) == 0:
            message = input("Type your message: ").lower()

        while shift < 0:
            shift = input("Type the shift number: ")
            try:
                shift = int(shift)
                print(shift)
            except ValueError:
                shift = -1

        print(f"Here the {action}d result: {cipher(action, shift, message)}")

        while once_more not in ["yes", "no"]:
            once_more = input(
                "Type 'yes' if you want to go again. Otherwise  type 'no': "
            )
        if once_more == "no":
            print("Bye!")
            break


def cipher(action: str, shift: int, message: str) -> str:
    "Encode / decode a message."

    alphabet = list(ascii_lowercase)
    cipher_message = []

    if action == "decode":
        shift *= -1

    for char in message:
        if char not in alphabet:
            cipher_message.append(char)
            continue
        index = alphabet.index(char)
        cipher_message.append(alphabet[(index + shift) % len(alphabet)])

    return "".join(cipher_message)


if __name__ == "__main__":
    main()
