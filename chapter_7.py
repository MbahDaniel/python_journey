import random
num = random.randint(1,100)
print(num)

fruit = random.choice(["apple","grape","lemon","orange","cherry"])
print(fruit)

coin = random.choice(["Tail","Head"])
choose = input("choose a (head) or a (tail): ")
if choose == coin:
  print("You win: ")  
else:
  print("bad luck: ")
choose = "head"
print("head")
choose = "tail"
print("tail")


num = random.randint(1,5)
guess = int(input("enter a number: "))
if guess == num:
  print("Well done: ")
elif guess > 5:
  print("too high: ")
  guess = int(input("pick a second number:  "))
  if guess == num:
      print("correct: ")
  else:
      print("You lose: ")
elif guess < 5:
   print("Too low: ")
   guess = int(input("pick a second number:  "))
   if guess == num:
      print("correct: ")
   else:
      print("You lose: ")


num = random.randint(1,10)
okk = "yes"
while num == "yes":
   guess = int(input("enter a number: "))
   if guess == num:
      print("correct: ")

num = random.randint(1,10)
okk = "yes"
while num == "yes":
   guess = int(input("enter a number: "))
   if guess == num:
      print("correct: ")
   elif guess > num:
      print("Too high: ")
   else:
      print("Too low: ")

score = 0
quiz = random.choice({"2","3","7","6","8"})
num1 = random.randint(1,10)
num2 = random.randint(1,10)
ans = num1 + num2 
selected_number = int(input("enter a number: ")) 
if selected_number == ans:
   score = score + 1
print(f"you got {score} out of 5")


colour = random.choice(["Blue","Green","red","orange","purple"])
again = "yes"
while again == "yes":
 select_a_colour = input("select from this colours: blue,green,red,orange,purple: ")
 if  select_a_colour == colour:
    print("Well done: ")
    again = "no"
 else:
    if select_a_colour == "Blue":
       print("blue fans are the best")
    elif select_a_colour == "Green":
       print("Green snake in green grass isn't bad for you: ")
    elif select_a_colour == "red":
       print("red cant be found on you: ")
    elif select_a_colour == "orange":
       print("you can't be sweeter than orange: ")
    elif select_a_colour == "purple":
       print("you cant afford a purple jersey")





   
   