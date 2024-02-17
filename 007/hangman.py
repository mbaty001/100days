import random
from words import WORDS
from logo import HANGMAN_LOGO
from hangman_pics import HANGMANPICS


def print_word(word):
    """Print word in formatted fashion"""
    print(f"{''.join(word)}\n")


def main():
    """Entrypoint."""
    print(HANGMAN_LOGO)

    target_word = random.choice(WORDS).lower()
    guessed_letters = [" _ " for _ in target_word]
    failures = 0
    used_letters = []

    print_word("Try to guess the word :)")
    while failures < len(HANGMANPICS) - 1 and " _ " in guessed_letters:
        print_word(guessed_letters)
        guessed_letter = input("Guess a letter: ").lower()

        if guessed_letter in used_letters:
            print_word("You have already tried this letter.")
        elif guessed_letter in target_word:
            for index, letter in enumerate(target_word):
                if guessed_letter == letter:
                    guessed_letters[index] = f" {letter} "
        else:
            failures += 1

        print(HANGMANPICS[failures])
        used_letters += guessed_letter
        print_word(f"Your tries: {' '.join(used_letters)}")

    if " _ " not in guessed_letters:
        print_word(guessed_letters)
        print("\nYou win!\n")
    elif failures >= len(HANGMANPICS) - 1:
        print("\nYou lost!\n")
        print_word(f"Word was: {target_word}")


if __name__ == "__main__":
    main()
