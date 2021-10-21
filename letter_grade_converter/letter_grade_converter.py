print("Letter Grade Converter")
print()

continue_response = "y"

while continue_response == "y":
    number_grade = int(input("Enter numerical grade: "))
    if 100 >= number_grade >= 88:
        letter_grade = "A"
    elif 87 >= number_grade >= 80:
        letter_grade = "B"
    elif 79 >= number_grade >= 67:
        letter_grade = "C"
    elif 66 >= number_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "C"

    print("Letter grade: " + letter_grade)
    print()
    continue_response = input("Continue? (y/n): ").lower()
    print()

print("Bye!")
