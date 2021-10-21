def miles_to_feet(miles):
    return int(miles * 5280)

def main():
    print("Hike Calculator")
    print()
    miles = float(input("How many miles did you walk?: "))
    feet = miles_to_feet(miles)
    print(f"You have walked {feet} feet.")


if __name__ == "__main__":
    main()