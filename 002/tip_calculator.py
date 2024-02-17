"""
Calculate the amount of cash each person should give including tips.
"""

if __name__ == "__main__":
    print("Welcome to the tip calculator.")
    bill = float(input("What was the total bill? $"))
    no_of_people = int(input("How many people to split the bill? "))
    tip_percentage = (
        int(input("What percentage tip would you like to give 10, 12 or 15? ")) / 100
    )

    bill_with_tip = bill + bill * tip_percentage
    bill_per_person = bill_with_tip / no_of_people
    amount = round(bill_per_person, 2)
    print(f"Each person should pay: ${amount}")
