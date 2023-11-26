import csv
file = open("books.csv", "w")
new_books = ("to kill a mockingbird, Harper lee, 1960\n")
file.write(str(new_books))
new_books = ("A brief history of time, stephen hawking, 1960\n")
file.write(str(new_books))
new_books = ("The great Gatsby,F.Scott Ftzgerald, 1922\n")
file.write(str(new_books))
new_books = ("The man who mistook his wife for  hat,oliver sacks, 1985\n")
file.write(str(new_books))
new_books = ("pride and prejudice,jane Austen, 1813\n")
file.write(str(new_books))
file.close()

#question 2
file = open("Books.csv","a")
book = input("enter thename of the book: ")
author = input("what  is the name of the author: ")
year = input("which year was the book released: ")
file.write(str(f"{book},{author},{year}"))
file.close()

file = open("books.csv","r")
for row in file:
    print(row)
    file.close()

#Question 3
record = int(input("how mant records do you want to add: "))
file = open("books.csv","a")
for i in range (0,record):
    book = ("Enter the name of the book:  ")
    author = ("Enter author name: ")
    year = ("what year was the book released: ")
    file.write(str(f"{book},{author},{year}"))
    file.close()

file =open("books.csv", "r")
find_author = input("Enter a name: ")
reader = csv.reader(file)
count = 0
for row in  file:
    if find_author in str(row):
     print(row)
     count = count + 1
if count == 0:
   print("no more books: ")
   file.close()
   
#question 4
start_year = int(input("enter a starting year: "))
end_year = int(input("enter an ending year: "))
file = list(csv.reader(open("books.csv")))
tmp = []
for row in file:
   tmp.append(row)
   file.close()

c =  0
file = open("newbooks.csv","r")
for row  in tmp:
  if int(tmp[c][2]) >= start_year and int(tmp[c] [2]) <= end_year:
     print(tmp[c])
     c = c  + 1
     file.close()

#question 5
file = open("books.csv","r")
c = 0
for row in file:
   print(row)
   c = c + 1
   file.close()
   
#question 6
file = list(csv.reader(open("books.csv")))
tmp = []
for row in file:
   tmp.append(row)
   file.close()

x =0
delete_row = int(input("Enter  number of row: "))
file = open("newbooks.csv","r")
for row in tmp: 
   if tmp[x] == delete_row:
     del tmp[delete_row]
     x = x + 1

data_row = int(input("enter the Row OF the data you would  like to change: "))
data_column =  int(input("Enter a number of column: "))
new_data = input("Enter New Data for the column you want to change:   ")
x = 0
efosa = tmp[x][x]

for row in tmp:
   if row == tmp[data_row]:
      row[data_column] = new_data
      file.close()
x = 0
file = open("newfile.csv","w")
for row in tmp:
   file.write(str(f"{x}{0},[x][1],[x][2]\n"))
   x = x + 1
   file.close()


tmp = [
   ["book1", "author1", "date1"],
   ["book2", "author2", "date2"],
   ["book3", "author3", "date3"],
   ["book4", "author4", "date4"]
]

row = 2
column  = 2
#  ["book3", "author3", "date3"]

#question 7
name = input("Enter your name: ")

