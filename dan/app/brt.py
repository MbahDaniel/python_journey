while True:
 import random

set 

print(select_random)
while chances < 8:
    chances += 1
    guess = int(input("Guess a number: "))
    if random_number == guess:
     print("You won\n Bet higher to win more")
     break
    elif guess < random_number or guess > random_number:
       print("You Lose")
    if chances == 100:
       print("Better luck next time: ")
break
       
 