#question 1
import random

def get_number():
 num = int(input("enter a number: "))
 return num

def count(num):
  x = 1
  while x <= num:
    print(x)
    x = x + 1

def main():
  num = get_number
  count = (num)

main()

#question 2
def get_info():
  high = int(input("enter an  high number: "))
  low = int(input("enter a low number: "))
  comp_num = random.randint(high,low)
  return comp_num

def think():
  guess_number = int(input("I'm thinking of a number, What number am i thinking of:  "))
  return(guess_number)

def check(guess_number,comp_num):
  next = "true"
  while next == "true":
    if comp_num == guess_number:
     print("Correct, you win!")
     next = "false"
    elif comp_num < guess_number:
     guess_number = int(input("Too low!, try again: "))
    else:
      guess_number = int(input("Too high!,  Try again: "))

def main():
  comp_num = get_info()
  guess_number = check()
  check(guess_number,comp_num)

main()

#question 3
print("""
1) Addition
2) subtraction """)
enter= int(input("Enter 1 or 2: "))
if enter == 1:
  def addition():
    random1 = random.randint(5,20)
    random2 = random.randint(5,20)
    ans = random1 + random2 
    answer = int(input("what is the sum of random1 and random2: "))
    answers = (f"This is your answer?{answer},this is the correct answer {ans}")
    return answers
  
def subtraction():
    random3 = random.randint(5,20)
    random4 = random.randint(1,25)
    ans = random3 - random4 
    answer = int(input("what is the sum of random1 and random2: "))
    answers = (f"This is your answer?{answer},this is the correct answer {ans}")
    return answers

def cross_check(answer, ans):
  if ans == answer:
    print("correct!: ")
  else:
    print(f"Incorrect, The correct answer is {ans}: ") 

def main ():
  print("""
1) Addition
2) subtraction """)
enter= int(input("Enter 1 or 2: "))
if enter == 1:
  answer, ans = addition()
  cross_check(answer,ans)  
elif enter == 2:
  answer,ans = subtraction
  cross_check(answer,ans)
else:
  print("Incorrect selection")

main()


#question 4
def add_name():
  addname = input("enter a name:  ")
  names.append(addname)
  return names

def change_name():
  num = 0
  for x in names:
    print(num,x)
  num = num + 1
  name_change = input("Enter the name you want to change: ")
  new_name = input("Enter the new name: ")
  names[name_change] = new_name
  return names

def delete_name():
  num = 0
  for x in names:
     print(num,x)
     num = num + 1
     del_name = input("which name do you want to delete from the list: ")
     del names[del_name]
     return names
  
def view_names():
  for x in names:
    print(x)


def main():
  again = "yes"
  while again == "yes":
   print("""
1) add name
2) change name
3) delete name
4) view name 
5) end 
        """)
  enter = int(input("Enter a number: "))
  if enter == 1:
    names = add_name()
  elif enter == 2:
    names = change_name()
  elif enter == 3:
    names = delete_name()
  elif enter == 4:
    names = view_names()
  elif enter == 5:
    again = "no"
  else:
    print("incorrect options: ")
  #incomplete

names = [] 
main()

#question 5





  

  

  
  


  
  
  
  



  
  

  


