print("welcome to the tip calculator!")

total_bill = float(input("what was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
split_bill = int(input("How many people you want to split the bill? "))

person_pay = round((total_bill + tip) / split_bill, 2)

print(f"Each person should pay: {person_pay}")