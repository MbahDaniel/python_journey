# #question 1
# name = input("enter a name: ")
# for i in range (1,4): 
#  print(name)

#  #question 2

# name1 = input("enter your name: ")
# user2 = int(input("enter a number: "))
# for i in range(1,user2 +1):
#   print(f"your name is  {name1}")

#   #question 3
# name2 = input("enter a name: ")
# for i in name2:
#  print(i)

# #question 4 
# num =  int(input("enter a number: "))
# name3 = input("enter a name: ")
# for i in name3:
#  for m in range  (1, num+1):
#   print(name3)
 
#  #question 5
#  num4 = int(input("enter a number between 1 and 12: "))
#  for i in range (1,13):
#   multiply = i * num4
#   print(f"multiplication table for{num4} is {multiply}: ")

   
#question 6
num5 = int(input(" enter a number less than 50: "))
for i in range (51,num5,-1):
  print(i)

#question 7
name4 = input("enter  your name: ")
num6= int(input("enter a number: "))
if num6 < 10: 
 for i in range (0,num6):  
  print(f"{name4}: ")
else:
 for i in range (1,4):
  print("too high: ")


#question 8
total = 0
for i in range (1,6):
  user4 = int(input("enter a number: "))
  user5 = input("""do you want the number included?
               1) yes
               2) no
               """)
  if user5 == "yes":
    total += user4
  elif user5 == "no":
    print("not added:")
  else:
    print("this is the total"),total

 #question 9
dir = input("""which  direction do you want 
            1) up
            2) down
            """)
if dir == "up":
  top = int(input("enter the topnumber: "))
  for i in range (1,top, +1):
    print(f"count up from 1 to {top}")
elif dir == "down":
  down = int(input("enter a number below 20: "))
  for i in range (20,down,-1):
    print(f"count down from  20 {down}: ")
else:
 print("i dont understand: ")

 #question 10
 attendant = int(input("How many people do you want to invite for this party"))
if attendant < 10:
  for i in range (1,attendant + 1):
   worker = input("enter a name: ")
   print(f"{worker} has been invited: ")
else:
   print("Too many people: ")