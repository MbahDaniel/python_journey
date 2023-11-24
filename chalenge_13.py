# file =open("numbers.txt","w")
# file.write("4, ")
# file.write("6, ")
# file.write("8, ")
# file.write("10, ")
# file.write("12, ")
# file.close()

# #question 2
# file = open("names.txt", "w")
# file.write("david\n")
# file.write("daniel\n")
# file.write("efosa\n")
# file.write("victor\n")
# file.write("nuel\n")
# file.close()

# #question 3
# file = open("Names.txt","r")
# print(file.read())
# file.close()

# #question 4
# file=open("name.txt","a")
# new_name = input("enter a new name: ")
# file.write(f"{new_name} \n")
# file.close()

# file = open("names.txt","r")
# print(file.read())
# file.close()

# #question 5
# print("""
# 1) create a new file
# 2) Display
# 3) Add a new item to the file make a selection 1,2 or 3: """)
# num = int(input("enter number 1 , 2 or 3: "))
# if num == 1:
#   school_subject = input("enter a school subject: ")
#   file = open("subject.txt","w")
#   file.write(f"{school_subject}\n")
#   file.close()
# elif num == 2:
#   file = open("subject.txt","r")
#   print(file.read())
#   file.close()
# elif num  == 3: # if the number selected is equal to 3
#   second_subject = input("enter another subject: ")
#   file = open("subject.txt", "w")
#   file.write(f"{second_subject}\n")
#   file.close()
#   file =  open("subject.txt","r")
#   print(file.read())
#   file.close()
# else:
#   print("Invalid option")

#   #question 6
#   file = open("names.txt","r")
#   print(file.read())

#   file =open("names.txt","w")
#   name = input("enter a name from the list:  ")
#   file = open("names2.txt","w")


#  How To Create and write to a text file
my_file = open("my_personal_file.txt", "w")
my_file.write("name1 \n")
my_file.write("name2 \n")
my_file.write("name3 \n")
my_file.write("name4 \n")
my_file.write("name5 \n")
my_file.close()

# How To Read A Text File
existing_file = open("my_personal_file.txt",  "r")
print(existing_file.read())

# How To Edit An Existing File
edit_existing_file = open("my_personal_file.txt", "a")
name = input("Name: ")
edit_existing_file.write(f"{name}  \n")
edit_existing_file.close()

# reead it again
print("\nReaading Edited Version")
new_existing_file = open("my_personal_file.txt",  "r")
print(new_existing_file.read())