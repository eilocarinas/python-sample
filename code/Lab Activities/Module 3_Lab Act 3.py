income = float(input("Enter the annual income : "))

min = 85528
if income < min:
    tax = (income * 0.18)-556.2
elif income <= 0:
    tax = 0
else:
    tax = 14839.2 + (0.32*(income-min))
tax = round(tax, 0)
print("The tax is: ", tax, "thalers")