#Example code just for list
x = [154,634,892,345,341,43] #Here we have created a list that contains numbers
print(len(x)) #This displays the length of the list
print(x[1:4])#This will display data in position 1,2,and  3. in this case 634,892 and 345.remember python starts counting from 0and stops when it gets to the last position,without showing the final value
for i in x:
    print (i)#Uses the items in the list in a for loop, useful if you want to print the items in a list on separate lines. 
num = int(input("enter a number: "))
if num == x: 
 print(f"{num} is in the list: ") 
else: 
 print("This is not in the list") #Asks the user to enter a number and checks whether the number is in the list and displays an appropriate message
x.insert(2,420) 
#Inserts the number 420 into position 2 and pushes everything else along to make space. This will change the index numbers of the items in the list. 
x.remove(892) 
#Deletes an item from the list. This is useful if you do not know the index of that item. If there is more than one instance of the data it will only delete the first instance. 
x.append(993) 
#Adds the number 993 to the end of the list.


#Example codes
color_tuple = ("orange","red","blue","yellow","green")
#Creates a variable name called “fruit_tuple” which stores four pieces of fruit within it. The round brackets define this group as a tuple and therefore the contents of this collection of data cannot be altered while the program is running
print(color_tuple.index("blue"))
#Displays the index (i.e. the numeric key) of the item “blue”. In this example it will return the number 2 as Python starts counting the items from 0, not 1.
print(color_tuple[2])
#Displays item 2 from “color_tuple”, in this case “blue”. 
attendance_list = ("daniel","philip","victor")#Creates a list of the names and stores them in the variable “names_list”. The square brackets define this group of data as a list and therefore the contents can be altered while the program is running.
attendance_list.append(input("Add a name: ")) #Asks the user to enter a name and will add that to the end of “attendance_list”.
del attendance_list[1] 
#Deletes item 1 from “attendance_list”. Remember it starts counting from 0 and not 1. In this case it will delete “Tim” from the list.
attendance_list.sort() 
#Sorts name_list into alphabetical order and saves the list in the new order. This does not work if the list is storing data of different types, such as strings and numeric data in the same list. 
print(sorted(attendance_list)) 
#Displays attendance_list in alphabetical order but does not change the order of the original list, which is still saved in the original order. This does not work if the list is storing data of different types, such as strings and numeric data in the same list.
colours = ("""
1) red
2) blue
3) green
           """)#Creates a dictionary called “colours”, where each item is assigned an index of your choosing. The first item in each block is the index, separated by a colon and then the colour
colours[2]="yellow"#Makes a change to the data stored in position 2 of the colours dictionary. In this case it will change “blue” to “yellow”.
