import random

from hangmanWords import word_list
from hangmanArt import stages, logo


# step 4 todo1:- create a variable called lives to keep track of the numbers of lives left,
# ste lives = 6


lives = 6

# Import the logo from hangmanArt.py and print it at the start of the game

print(logo)

# step 1 todo 1:- Randomly choose a word form the word_list and assigned to variable called chosen_word

chosen_word = random.choice(word_list)
print(chosen_word)


# step 2 Todo 1:- create a "placeholder" with the same number of blanks as the chosen_word

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess: " + placeholder)

# step 3 Todo 1:- use a while loop to let the user guess again
game_over = False
correct_letters = []

# step 1 todo 2:- ask the user to guess the letter and assign their answer to a variable called guess.
#  make guess lowercase

while not game_over:
    print(f"**********************************{lives}/6 LIVES LEFT***************************************")
    guess = input("Guess the letters: ").lower()

    if guess in correct_letters:
        print(f"Yov've already guessed {guess}")

    # step 2 Todo 1:- create a "display" that puts the user latter in right position

    display = ""

    # step 1 todo 3:- check if the letter user generated is ont of the letters in the chosen_word.
    # print "right" if it is or "wrong" if it's not

    # step 3 Todo2:- change the for loop so that you keep the previous correct values

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            # print('else')


    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1
        print(f"You've guessed {guess} that's not in the word. You lose the life.")

        # step 4 todo2:- If guess is not a letter in the chosen_word, then reduce lives by 1.
        # if live goes down to zero then the game should end and print "you lose"

        if lives == 0:
            game_over = True
            print(f"*********************************It was {chosen_word} / you lose*******************************")

    if "_" not in display:
        game_over = True
        print("********************************You Win********************************")

    # step 4 todo3:- print the ascii art grom the list stages that corresponds to the
    # current number of live user has remaining.

    print(stages[lives])
