
import random



easy_hint = 10
hard_hint = 5

def check_answer(user_guess, actual_answer, turns):
    """check answer against guess, returns the number of turns ramaining"""
    if user_guess > actual_answer:
        print("Too high. \n Guess again.")
        return turns -1
    elif user_guess < actual_answer:
        print("Too Low. \n Guess again.")
        return turns -1
    elif user_guess == actual_answer:
        print(f"You got it! The answer was {actual_answer}")


# function to set the dificulty

def set_dificulty():
    chose_dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if chose_dificulty == "easy":
        return easy_hint
    if chose_dificulty == "hard":
        return hard_hint

def game():
    answer = random.randint(1, 100)
    print(answer)
    print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")

    turns = set_dificulty()



    guess = 0        

    while guess != answer:
        guess = int(input("Make a guess: "))
        print(f"You have {turns} attempts remaining to guess the number.")
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Run out of guess you lose!")
            return
        elif guess != answer:
            print("guess again")

game()