import conversions

def title():
    print("Feet and Meters Converter")

def menu():
    print()
    print("Conversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")

def main():
    title()
    response = "y"
    while response == "y":
        menu()
        selection = input("Select a conversion (a/b): ").lower()
        print()
        if selection == "a":
            feet = float(input("Enter feet: "))
            meters = round(conversions.feet_to_meters(feet), 2)
            print(f"{meters} meters")
            print()
        else:
            meters = float(input("Enter meters: "))
            feet = round(conversions.meters_to_feet(meters), 2)
            print(f"{feet} feet")
            print()     
        response = input("Would you like to perform another conversion? (y/n): ")
    print()
    print("Thanks, bye!")


if __name__ == "__main__":
    main()