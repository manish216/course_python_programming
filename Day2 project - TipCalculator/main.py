# Display message : Welcome to the tip calculator.
# Ask the input message: What was the total bill?
# Ask the input message: What percentage tip would you like to give? 10, 12, or 15?
# Ask the input message: How many people to split the bill?
# display output : Each person should pay: $amount

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill?")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")

print(f"Each person should pay: ${round((float(total_bill) * (1+float(tip_percentage)/100))/int(people),2)}")

# instead of using round fn. we can use format "{:.2f}".format(variable)
print(f"Each person should pay: ${"{:.2f}".format((float(total_bill) * (1+float(tip_percentage)/100))/int(people))}")
