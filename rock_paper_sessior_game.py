import random


rock = """
   -----   
 /       \ 
|  ROCK   |
 \       / 
   -----   
"""

paper = """
 -----------  
 |           | 
 |  PAPER    | 
 |           | 
 |  -------  | 
 |  -------  | 
 |  -------  | 
 |           | 
  -----------  
"""


scissors = """
     \ /     
      X      
     / \     
    (   )    
    (   )    
     SCISSORS
"""




game_images = [rock, paper, scissors]

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

rand_int = random.randint(0, 3)

print(f"Computer choose {game_images[rand_int]}")

if choose >= 0 or choose <= 2:
    print(game_images[choose])


if choose >= 3 or choose < 0:
    print("you typed invalid number")
elif choose == 0 & rand_int == 2:
    print("You Win")
elif choose < rand_int:
    print("You Lose")
elif choose == rand_int:
    print("Draw")
elif rand_int == 0 & choose == 2:
    print("You Lose")
elif choose > rand_int:
    print("You Win")


