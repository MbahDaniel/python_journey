#question 1
grades = [[2,5,8], [3,7,4],[1,6,9],[4,2,0]]
print(grades)

#question 2
grades = [[2,5,8], [3,7,4],[1,6,9],[4,2,0]]
row = int(input("enter a number from 0 to 3"))
column = int(input("enter a number from 0 to 2: "))
print(grades[row][column])

#question 3
grades = [[2,5,8], [3,7,4],[1,6,9],[4,2,0]]
row = int(input("enter a number from 0 to 3"))
print[row]
new_value = int(input("enter a number from 0 to 3: "))
grades[row].append[new_value]
print(grades[row])

#question 4
grades = [[2,5,8], [3,7,4],[1,6,9],[4,2,0]]
row = int(input("enter a number from 0 to 3"))
print(grades[row])
column = int(input("enter a number from 0 to 2: "))
print(grades[row][column])
change = ("Do you want to  change the value(yes/no)")
if new_value == "yes":
    new_value = int(input("enter a new value: "))
    grades[row][column] = new_value
    print(grades[row])

#question 5
sales_record = {"john":{"N":3056, "S":8463,"E":8441, "W":2694}, "Tom":{"N":4832, "S": 6786,"E":4737, "W":3612}  , "Anne" : {"N":5239,"S":4802,"E":5820,"W":1859}, "Fiona":{"N":3904,"S":3645,"E": 8821,"W":2451}}

#Question 6
sales_record = {"john":{"N":3056, "S":8463,"E":8441, "W":2694}, "Tom":{"N":4832, "S": 6786,"E":4737, "W":3612}  , "Anne" : {"N":5239,"S":4802,"E":5820,"W":1859}, "Fiona":{"N":3904,"S":3645,"E": 8821,"W":2451}}
print("John,Tom,Anne,Fiona")
name = input("enter a name frome the names above: ")
print("N,S,E,W")
region = ("Enter a region from the ones above: ")
print(sales_record[row][region])
alter_name = input("change the record  on which name: ")
alter_region = input("change the record on which region?: ")
sales_figure =("enter correct sales figure: ")
sales_record[alter_name][alter_region] = sales_figure
print(sales_record[name])

#question 7
list = {}
for i in range (0,4):
    name = input("Enter a name: ")
    age = input("Enter age: ")
    shoe_size = ("Enter shoe size: ")
    list[name] = [{"Age":age,"Shoe_size":shoe_size}]
    #NOT COMPLETED



#question 8
list = {}
for i in range (0,4):
    name = input("Enter a name: ")
    age = input("Enter age: ")
    shoe_size = ("Enter shoe size: ")
    list[name] = [{"Age":age,"Shoe_size":shoe_size}]
remove = input("enter a name you would like tonremove: ")
del list[remove]

