
import random
from gamedata import higher_lower_data
from art import logo, vsSymbol



def format_data(account):
    """Format the account data into the printable format"""
    account_name = account["name"]
    account_value = account["value"]
    # return f"{account_name} & followers: {account_value}"
    return f"{account_name}"


# check if user is correct
def check(user_guess, a_followers, b_followers):
    """Take a user guess and the followers counts and returns if they got it right"""

    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"



print(logo)
score = 0


account_b = random.choice(higher_lower_data)
# Make the game repeatable
continue_game = True
while continue_game:


    # Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(higher_lower_data)

    if account_a == account_b:
        account_b = random.choice(higher_lower_data)


    # format the accounty data into printable format


    print(f"Compare A: {format_data(account_a)}")
    print(vsSymbol)
    print(f"Compare B: {format_data(account_b)}")


    # ask the user for guess

    guess = input("Who has more followers? Type 'A' or 'B'").lower()


    # - get value of each account

    followers_a = account_a["value"]
    followers_b = account_b["value"]


    # - use if to check if the user is correct

    is_correct =  check(guess, followers_a, followers_b)

    # score Keeping

    if is_correct:
        score += 1
        print(f"You are right! Current Score: {score}")
    else:
        print(f"Sorry!, thats wrong. Final Score: {score}")
        continue_game = False







# give user feedback on there guess




 