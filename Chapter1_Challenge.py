# question 1 
Firstname = input ("what is your first name")#Type your firstname
print ("Hello", Firstname)

#question 2
surname = input ("what your surname")#input your surname
print ("My names are")
print (Firstname + surname) #Add firstname to  surname

# Question 3
answer = "A Gummy bear"
print ("what do you call a bear with no teeth\n", answer)

#Question 4
B = int(input("Enter a number: "))
A = int(input("Enter a number: "))
C = B + A
print ("The total is", C)

#question 5
D = int(input("Enter first number: "))
E = int(input("Enter second number: "))
F = int(input("Enter third number: "))
ans = (D + E) * F
print ("when you add the first and second number then mutilply by the third number the answer is", ans)

# Question 6
started = int(input(" number of pizza started with: "))
eaten = int(input("Number of slice eaten: "))
remaining = started - eaten
print(f'you have {remaining} left')

# question 7
name = input ("what is your name")
age = int(input(" how old are you"))
newage = age + 1 
print(f"{name} next birthday you would be {newage}")

#question 8
bill = int(input("what is the total price of the bill: ")) # asking how much for the bill
Dinner = int(input("how many dinners: "))
newbill = bill / Dinner
print(f"how much each person must pay: {newbill}")

#question 9
numdays = int(input("what is the number of days"))
hour = 24 * numdays
minute = 1440 * numdays
seconds =  86400 * numdays
print(f"{hour} number of days in hour: ")
print(" number of minutes", minute )
print ("number of seconds", seconds)

#question 10
weight = int(input("what is the weight of your item in kg"))
pounds = weight * 2,204
print(f"{pounds} number of weight in pounds: ")

#question 11
over = int(input("enter a number over 100: "))
under = int(input("enter a number under 10: "))
G = over//under

print(f"The number  of {under} in {over} is: {G}")





