print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
print("Type left or right")

direction = str(input())

if direction.lower() == "left":
    print("You've come to lake. There is an island in the middle of the lake.")
    print("Type wait to wait for a boat. Type swim to swim across.")
    step2 = str(input())
    if step2.lower() == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        print("One red, one yellow and one blue. Which colour do you choose?")
        step3 = str(input())

        if step3.lower() == "red":
            print("It's a room full of fire. Game Over.")
        elif step3.lower() == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")

    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
