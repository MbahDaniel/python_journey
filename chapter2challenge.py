#question 1 
number = int(input("type first number: "))
number1 =int(input("type second numbe4r: "))
if number > number1:
   print(f"{number1} next number is {number} ")
else:
  print(f" first number  would be {number} the second would be {number1}")

#question 2 
num1 = int(input("enter number less than 20: "))
if num1 >= 20:
   print("too high: ")
else: 
  print("Thank you")

#question 3
num = int(input("type number between 10 and 20 inclusive: "))
if num >= 10 and num <= 20:
   print ("thank you")
else:
   print ("incorrect")

#Question 4
color = input("enter your favourite colour").upper()
if color == "RED":
  print(" I like red too")
else:
   print (f" i dont like {color} i prefer red")

# #Question 5
rain = input("is it raining: ").lower()
if rain == "yes":
    windy = input("Is It Windy?: ")
    if windy == "yes":
      print("It Is too windy for an umbrella")
    else:
      print("take aan umbrella")
      if windy != "yes":
         print ("enjoy your  day: ")

# question 6
age  = int(input("whats your age"))
if age >= 18:
   print("you can vote: ")
elif age == 17:
 print("you can learn to drive: ")
elif age == 16: 
   print("you can buy alottery ticket: ")
else:
    print  ("you can go trick or- treating: ")

#question 7
num = int(input("enter  number: "))
if num < 10:
  print("Too low: ")
elif num > 10 and num < 20:
 print("correct") 
else:
   print("Too high") 

#question 8
num  = int(input("enter a number: ")) #ask user to enter a number
if num == 1:
   print("thank you")
elif num == 2:
   print("welldone: ")
elif num == 3:
   print("correct")
else:
   print("error message: ")



