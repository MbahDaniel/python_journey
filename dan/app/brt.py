while True:
 import random
 from pydantic import BaseModel
 from typing import Optional
 from random import randrange

 class bet_account(BaseModel):
    Name:str
    phone_number: int
    saved: bool = True
    referal_code : Optional[int] = None
    accont_balannce: 0

 existing_account =[{"name":"danny", "phone_number": "09086754566", "id": 1}]

set 


print(select_random)
place_bet = int(input("Enter an amount: "))
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

       
 
 