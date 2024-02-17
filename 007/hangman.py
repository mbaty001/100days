import random

HANGMAN_WORD = """
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
"""

HANGMANPICS = [
    "",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
]

WORDS = [
    "mama",
    "tata",
    "apator",
    "ziolko",
    "koziolek",
    "lupin",
    "poniedzialek",
    "zelazko",
    "szafa",
]


def print_word(word):
    """Print word in formatted fashion"""
    print(f"{''.join(word)}\n")


def main():
    """Entrypoint."""
    print(HANGMAN_WORD)

    target_word = random.choice(WORDS)
    guessed_letters = [" _ " for _ in target_word]
    failures = 0

    print_word("Try to guess the word :)")
    while failures < len(HANGMANPICS) - 1 and " _ " in guessed_letters:
        print_word(guessed_letters)
        guessed_letter = input("Guess a letter: ").lower()

        if guessed_letter in target_word:
            for index, letter in enumerate(target_word):
                if guessed_letter == letter:
                    guessed_letters[index] = f" {letter} "
        else:
            failures += 1

        print(HANGMANPICS[failures])

    if " _ " not in guessed_letters:
        print_word(guessed_letters)
        print("\nYou win!\n")
    elif failures >= len(HANGMANPICS) - 1:
        print("\nYou lost!\n")


if __name__ == "__main__":
    main()
