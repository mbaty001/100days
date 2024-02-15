import random


def print_ascii(number, who):
    print(f"{who} choice: ")
    if number == 0:
        print("""
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif number == 1:
        print("""
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    elif number == 2:
        print("""
Papper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")


def main():
    your_choice = int(input("What is your choice: 0-rock, 1-scissors or 2-paper? "))
    print_ascii(your_choice, 'Your')
    ai_choice = random.randint(0, 2)
    print_ascii(ai_choice, 'AI')

    if your_choice == ai_choice:
        print("Draw!")
    elif (your_choice == 0 and ai_choice == 1) or \
         (your_choice == 1 and ai_choice == 2) or \
         (your_choice == 2 and ai_choice == 0):
        print("You win!")
    else:
        print("AI win!")


if __name__ == "__main__":
    main()
