# import csv
# file = open("books.csv", "w")
# new_books = ("to kill a mockingbird, Harper lee, 1960\n")
# file.write(str(new_books))
# new_books = ("A brief history of time, stephen hawking, 1960\n")
# file.write(str(new_books))
# new_books = ("The great Gatsby,F.Scott Ftzgerald, 1922\n")
# file.write(str(new_books))
# new_books = ("The man who mistook his wife for  hat,oliver sacks, 1985\n")
# file.write(str(new_books))
# new_books = ("pride and prejudice,jane Austen, 1813\n")
# file.write(str(new_books))
# file.close()

# #question 2
# file = open("Books.csv","a")
# book = input("enter thename of the book: ")
# author = input("what  is the name of the author: ")
# year = int(input("which year was the book released: "))
# file.write(str(f"{book},{author},{year}"))
# file.close()

# file = open("books.csv","r")
# for row in file:
#     print(row)
#     file.close()

# #Question 3
# record = int(input("how mant records do you want to add: "))
# file = open("books.csv","a")
# for i in range (0,record):
#     book = ("Enter the name of the book:  ")
#     author = ("Enter author name: ")
#     year = ("what year was the book released: ")
#     file.write(str(f"{book} + {author} + {year}"))
#     file.close()

# find_author = input("Enter a name: ")
# file =open("books.csv", "r")
# count = 0
# for row in  file:
#     if find_author in str(row):
#      print(row)
#      count = count + 1
# if count == 0:
#    print("no more books: ")
#    file.close()
   
# #question 4
# start_year = int(input("enter a starting year: "))
# end_year = int(input("enter an ending year: "))
# file = list(csv.reader(open("books.csv")))
# tmp = []
# for row in file:
#    tmp.append(row)

# #question 5
# file = open("books.csv","r")
# count = 0
# for i in file:
#    pass


tmp = []

"me, myself, i"
"i,  you,  them"

tmp =[
    ["me", "myself", "i"], 
    ["i", "you", "them"],
]

line = f"{tmp[0][0]}, {tmp[0][1]}, {tmp[0][2]}"
