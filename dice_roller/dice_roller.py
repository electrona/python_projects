import random


def dice_roll():
    return random.randint(1, 6)


def special_message(dice_total):
    if dice_total == 2:
        print("Snake eyes!")
    elif dice_total == 12:
        print("Boxcars!")


def main():
    print("Dice Roller")
    print()
    response = input("Roll the dice? (y/n): ")
    while response == "y":
        print()
        die1 = dice_roll()
        die2 = dice_roll()
        dice_total = die1 + die2
        print(f"Die 1: {die1}")
        print(f"Die 2: {die2}")
        print(f"Total: {dice_total}")
        special_message(dice_total)
        print()
        response = input("Roll again? (y/n): ")


if __name__ == "__main__":
    main()
