print("Change Calculator")
print()

continue_response = "y"

while continue_response == "y":
    cents = int(input("Enter number of cents:\t"))
    print()
    quarters = (cents // 25)
    dimes = (cents - (quarters * 25)) // 10
    nickels = (cents - (quarters * 25) - (dimes * 10)) // 5
    pennies = (cents - (quarters * 25) - (dimes * 10) - (nickels * 5))

    print("Quarters:\t" + str(quarters))
    print("Dimes:\t\t" + str(dimes))
    print("Nickels:\t" + str(nickels))
    print("Pennies:\t" + str(pennies))
    print()
    continue_response = input("Continue? (y/n): ").lower()
    print()

print("Bye!")
