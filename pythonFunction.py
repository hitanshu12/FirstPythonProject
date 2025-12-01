

# create a function

def greet():
    print("hello")
    print("How do you do?")
    print("Isn't the weather nice?")


greet()

print()


def greet_with_name(name):       # name is parameter
    print(f"hello {name}")
    print("How do you do?")
    print("Isn't the weather nice?")


greet_with_name("Pooja")  # "Pooja" is argument


print()


def greet_with(name, location):       # name is parameter
    print(f"hello {name}")
    print(f"what is it like in {location}?")


greet_with("Pooja", "delhi")  # "Pooja" is argument
