print("welcome to Pyhton Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on there size choice.

bill = 0

if size == "S":
    bill = bill + 15
elif size == "M":
    bill = bill + 20
elif size == "L":
    bill = bill + 25
else:
    print("You type the wrong inputs!")

# todo: work out how much to add to their bill based on there pepperoni choice.

if pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:
        bill = bill + 3

# todo: work out their final amount basedd on whether if they want extra cheese.

if extra_cheese == "Y":
    bill = bill + 1


print(f"your final bill is ${bill}.")


print("====================================Logical Operator========================================")





