import random

letters_lower = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

print("Welcome to my password Generator!")

nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbol = int(input("How many symbols would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))


# Easy Level
# password = ""
#
# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters_lower)
#     password = password + random_char
#
# for sym in range(1, nr_symbol + 1):
#     random_sym = random.choice(symbols)
#     password = password + random_sym
#
# for num in range(1, nr_numbers + 1):
#     random_num = random.choice(numbers)
#     password = password + str(random_num)
#
# print(f"your password is {password}")

# Hard level

password_list = []

for char in range(1, nr_letters + 1):
    random_char = random.choice(letters_lower)
    password_list.append(random_char)

for sym in range(1, nr_symbol + 1):
    random_sym = random.choice(symbols)
    password_list.append(random_sym)

for num in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    password_list.append(str(random_num))

print(password_list)
# shuffle the list randomly
random.shuffle(password_list)
print(password_list)

# convert password list into string
password = ""
for pass_char in password_list:
    password = password + pass_char

print(f"your generated password is {password}")
