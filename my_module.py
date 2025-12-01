my_fav_num = [23, 40, 50, 20, 60, 90, 70]

# sum
sum_num = 0
for i in my_fav_num:
    sum_num = sum_num + i

print(sum_num)

# Max

max_num = 0

for x in my_fav_num:
    if x > max_num:
        max_num = x

print(max_num)



# using for loop with the range function

for i in range(0, 11, 3):
    print(i)


#add number form 1 to 100

total = 0
for num in range(1, 101):
    total += num

print(total)

print("FizzBuzz Program")
print()



for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# While Loop

print("while Loop")












