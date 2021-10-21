def is_even(number):
    if (number % 2 == 0):
        return True
    else:
        return False

def main():
    print("Even or Odd Checker")
    print()
    user_entry = int(input("Enter an integer: "))
    if is_even(user_entry) == True:
        print("This is an even number.")
    else:
        print("This is an odd number.")


if __name__ == "__main__":
    main()