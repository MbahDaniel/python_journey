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
print(file.red())
file.close()

#question 4
file=open("name.txt","w")
new_name = input("enter a new name: ")
file.write(f"{new_name} \n")

#question 5
file = open("names.txt")