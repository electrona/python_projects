# print heading
print("Pay Check Calculator")
print()

# receive input
hours_worked = float(input("Hours Worked:\t\t"))
hourly_pay_rate = float(input("Hourly Pay Rate:\t"))
print()

# perform pay calculations
gross_pay = round((hourly_pay_rate * hourly_pay_rate),2)
tax_rate = 18
tax_amount = round((gross_pay * (tax_rate / 100)),2)
take_home_pay = round((gross_pay - tax_amount),2)

# print results
print("Gross pay:\t\t" + str(gross_pay))
print("Tax Rate:\t\t" + str(tax_rate) + "%")
print("Tax Amount:\t\t" + str(tax_amount))
print("Take Home Pay:\t\t" + str(take_home_pay))

