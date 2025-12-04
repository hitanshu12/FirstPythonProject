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



print(pow(2, 4))




s = ""
for ch in ["a", "b", "c"]:
    s += ch
print(s)


# Dictionary

programing_dictionary = {
    "bug": "An Bug",
    "Function": "An Function",
    "Loop": "An Loop",
}


print(programing_dictionary["Loop"])

# add key value in dictionary

programing_dictionary["exception"] = "An exception"
print(programing_dictionary)


# empty dict

empty_dict = {}
print(empty_dict)

# edit item key is bug

programing_dictionary["bug"] = "An Moth"
print(programing_dictionary)


# using loop through dictionary


for thing in programing_dictionary:
    print(thing)     # through only dictionary keys

for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])    # give the value of the dictionary keys


for item in programing_dictionary.items():
    print(item)
    # print(programing_dictionary[key])    # give the value of the dictionary keys

for value in programing_dictionary.values():
    print(value)  # only values of dict31



# Nested List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "India": ["Delhi", "Mumbai", "Bangalore"],
    "UK": ["London", "Manchester", "Wales"],
    "Germany": ["Berlin", "Stuttgart"]
}

# access delhi
print(travel_log["India"][0])

# access Lille
print(travel_log["France"][1])


# print "D" from Nested List

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Nested Dictionary

travel_log1 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "num_times_visited": 2
    },
    "India": {
        "cities_visited": ["Delhi", "Mumbai", "Bangalore"],
        "num_times_visited": 8
    }
}

print(travel_log1["India"]["cities_visited"][2])




























