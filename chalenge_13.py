file =open("numbers.txt","w")
file.write("4, ")
file.write("6, ")
file.write("8, ")
file.write("10, ")
file.write("12, ")
file.close()

#question 2
file = open("names.txt", "w")
file.write("david\n")
file.write("daniel\n")
file.write("efosa\n")
file.write("victor\n")
file.write("nuel\n")
file.close()

#question 3
file = open("Names.txt","r")
print(file.read())
file.close()

#question 4
file=open("name.txt","a")
new_name = input("enter a new name: ")
file.write(f"{new_name} \n")
file.close()

file = open("names.txt","r")
print(file.read())
file.close()

#question 5
print("""
1) create a new file
2) Display
3) Add a new item to the file make a selection 1,2 or 3: """)
num = int(input("enter number 1 , 2 or 3: "))
if num == 1:
  school_subject = input("enter a school subject: ")
  file = open("subject.txt","w")
  file.write(f"{school_subject}\n")
  file.close()
elif num == 2:
  file = open("subject.txt","r")
  print(file.read())
  file.close()
elif num  == 3: # if the number selected is equal to 3
  second_subject = input("enter another subject: ")
  file = open("subject.txt", "w")
  file.write(f"{second_subject}\n")
  file.close()
  file =  open("subject.txt","r")
  print(file.read())
  file.close()
else:
  print("Invalid option")

  #question 6
  file = open("names.txt","r")
  print(file.read())
  file.close()

  file =open("names.txt","w")
  name = input("enter a name from the list:  ")
  file = open("names2.txt","w")
  