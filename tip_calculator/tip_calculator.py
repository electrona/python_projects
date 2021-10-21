# print header
print("Tip Calculator")
print()

# receive input
cost_of_meal = float(input("Cost of meal:\t\t"))
tip_percentage = float(input("Tip percentage:\t\t"))
print()

# perform calculations
tip_amount = round((cost_of_meal * (tip_percentage / 100)),2)
total_amount = round((cost_of_meal + tip_amount),2)

# print results
print("Tip amount:\t\t" + str(tip_amount))
print("Total amount\t\t" + str(total_amount))