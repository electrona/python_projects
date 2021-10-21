#print header
print("Travel Time Calculator")
print()

#receive input
miles = int(input("Enter miles:  "))
miles_per_hour = int(input("Enter miles per hour:  "))
print()

#calculate results
hours = miles // miles_per_hour
minutes = (miles % miles_per_hour)

#print results
print("Estimated travel time")
print("Hours:  " + str(hours))
print("Minutes:  " + str(minutes))