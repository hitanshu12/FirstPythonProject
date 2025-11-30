height = float(input("Enter you height: "))
weight = float(input("enter your weight: "))

height_sqr = height ** 2

bmi = round(weight/height_sqr,0 )

print(bmi)