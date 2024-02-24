print("Question 1")
total = 0
while total <= 50:
  num = int(input("enter a number: "))
  total = total + num
  # total+=num
  print(f"the total is {total} ")

#question 2
print("Question 2")
num1 = 0
while num1 <= 5: 
  num1 = int(input("Enter a number: "))
  print(f"The last number you entered was  {num1}: ")

#question 3
("Question 3")
first_number = int(input("enter a number: "))
total = first_number
next_number = "y"
while total == "y":
  second_number = int(input("enter a number: "))
  total = total + second_number
  next_number = input("do you want another number: ")
  print(f"This is the {total} total: ")

  #Question 4
  count = 0
  next = "yes"
  while count == "yes":
    name = input("What is the name?: ")
    print(f"{name} Has now been invited: ")
    count = count + 1
    next = input("Do you want to invite another name: ")
    print(f"Total number people attending the party is {count}")

  #question 5
  compnum = 50
  count  = 0
  guess = int(input("Guess  a number: "))
  while guess != 50:
    if guess  < 50:
      print("Too low: ")
    else:
     print ("Too high: ")
    count = count + 1
    guess = int(input("guess again: "))
    print("Well done", count)
    

    #question 6
    num = int(input("Enter  a number between 10 aand 20: "))
    while num < 10 or num >20:
      if num < 10:
       print("Too low! plesas: ")
      else:
        print("Too high!: ")
      num = int(input("Try  again: "))
      print("Thank you:")

      #QUESTION 7
      num_of_bottle = 10
      count = -1
      while num_of_bottle == 10:
        print(f"there are {num} green bottles hanging on a wall:  ")
        print(f"{num}green bottles hanging on a wall and if 1 green bottle should accidentally fall: ")
        count = count + num_of_bottle
        remaining_bottle = int(input("enter number of remaing bottle: "))
        if remaining_bottle == count:
          print(f"There will be {count} green bottles hanging on the wall:")
        else:
         remaining_bottle = int(input("No, try again: "))
         print("There are no more green bottles sitting on the wall: ")