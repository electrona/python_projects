# print heading
print("Registration Form")
print()

# receive input 
first_name = input("First name:\t")
last_name = input("Last name:\t")
birth_year = input("Birth year:\t")
print()

# print results
print("Welcome " + first_name + " " + last_name + "!")
print("Your registration is complete.")
print("Your temporary password is: " + first_name + "*" + birth_year)