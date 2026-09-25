def income_tax(value):
    if value < 12500:
        return "You do not need to pay tax"
    elif 12500 < value < 50270:
        return f"You have to pay 20% of your income as income tax, which is £{float(value*0.2)}"
    elif 50271 < value < 125140:
        return f"You have to pay 40% of your income as income tax, which is £{float(value * 0.4)}"
    elif value > 125140:
        return f"You have to pay 45% of your income as income tax, which is £{float(value * 0.45)}"
    else:
        return "Error, enter a number"


tax = income_tax(30000)
print(tax)