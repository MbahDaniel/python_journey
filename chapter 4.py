import math
num = float(input("enter a number with decimal place: "))
ans = num * 2 
print(ans)

#question 2
num = float(input("enter number with more than 2 decimal place: "))
ans1 = num * 2
print(round(ans1,2))

#question 3
dan = int(input("enter an integer over 500: "))
answer = math.sqrt(dan)
print(round(answer,2))

#question 4
pi = math.pi
print(round(pi,5))

#Question 5
Rad = int(input("enter the radius of a circle: "))
area = math.pi * (Rad**2)
print(f"this is the area {area}")

#Question 6
num1 = int(input("enter a numbers: "))
num2 = int(input("enter second number"))
divide =num1//num2
remain = num1 % num2
print(f" {num1} divided by {num2} is {divide} remaining {remain}: ")

#question 7
rad = int(input("enter the radius: "))
depth = int(input("enter  depth of cylinder: "))
circle_area = math.pi * (rad**2)

print(f"Total Volume : {circle_area*depth} ")

#Question 8
print("""
1) Square
2) Triangle
""")

shape_choice = int(input("Choose One: "))
if shape_choice == 1:
  length = int(input("whats the lenth  of the sides"))
  print(f"This is the area {length**2}")
elif shape_choice == 2:
    num5 = int(input("whats the base of  the triangle: "))
    num6 =  int(input("enter height of triangle: "))
    print(f"this is the area{num5/2 * num6}:  ")
else:
    print("please try again later: ")


    












