import sqlite3
with sqlite3.connect("phone.db") as db:
    cursor = db.cursor()#connects to the phone database, if no such database exist,  create  a one.The file would be stored in the same folder as the  program
cursor.execute(""" CREATE TABLE IF NOT EXISTS phone(
 id integer PRIMARY KEY,
 firstname text NOT NULL,
 surname text NOT NULL,
 phonenumber integer);""")

cursor.execute("""INSERT INTO phone(id,firstname,surname,phonenumber)
 VALUES("1","Simon","Howels","01223349752")""")
db.commit()

cursor.execute("""INSERT INTO phone(id,firstname,surname,phonenumber)
  VALUES("2","Karen","phillips","01954295773")""")
db.commit()

cursor.execute("""INSERT INTO phone(id,firstname,surname,phonenumber)
  VALUES("3","Darren","smith","01583749012")""")
db.commit
cursor.execute("""INSERT INTO phone(id,firstname,surname,phonenumber)
  VALUES("4","Anne","jones","01323567322")""")
db.commit
cursor.execute("""INSERT INTO phone(id,firstname,surname,phonenumber)
  VALUES("5","Mark","smith","01223855534")""")
db.commit()

db.close


#question 2
def viewphonebook():
    cursor.execute("select*from phonebook")
    for x in cursor.fetchall():
        print(x)

def add_to_phonebook():
    newid = int(input("Enter ID: "))
    newfname = input("Enter Firstname: ")
    newsname = input("Enter your surname: ")
    phone_number = int("Enter phone number: ")
    cursor.execute("""insert into employees(id,firstname,surname,phonenumber)
    Values(?,?,?,?)""",(newid,newfname,newsname,phone_number))
    db.commit()

def searchsurname():
    selectsurname = input("Enter the name your searching for: ")
    cursor.execute("SELECT * FROM Phonebook where Surname = ?",[selectsurname] )
    for i in cursor.fetchall():
        print(i)

def deleteperson():
    selectid = int("Enter ID number: ")
    cursor.execute("DELETE * FROM phonebook where id = ?",[selectid])
    cursor.execute("SELECT * FROM phonebook")
    for i in cursor.fetchall():
        print(i)

    db.commit()

with sqlite3.connect("phonebook.db") as db:
    cursor = db.cursor()

def main():
    again = "yes"
    while again == "yes":
     print("""
           1) View phonebook
           2) Add to phone book
           3) Search for surname
           4) Delete person from phone book
           5) Quit
           """)
    select = int(input("Select a number: "))
    if select == 1:
        viewphonebook()
    elif select == 2:
        add_to_phonebook()
    elif select == 3:
        searchsurname()
    elif select == 4:
        deleteperson()
    elif select == 5:
        again = "no"
    else:
        print("Incorrect selection")

main()
db.close()

#question 3
with sqlite3.connect("bookinfo.db") as db:
    cursor = db.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXIST books(
        Name text PRIMARY KEY
        place of birth text NOT NULL);""")
cursor.execute("""INSERT INTO book(names,place of birth)
 Values("agatha Christie",Torquay)""")
db.commit()

cursor.execute("""INSERT INTO bookinfo(names,place of birth)
 Values "cecelia Ahern",Dublin""")
db.commit()
cursor.execute("""INSERT INTO bookinfo(names,place of birth)
 Values "agatha J.K.Rowling",Bristol""")
db.commit()
cursor.execute("""INSERT INTO bookinfo(names,place of birth)
 Values "Oscar Wilde",Dublin""")
db.commit()

cursor.execute("""CREATE TABLE IF NOT EXIST books(
  id integer Primary key,
  Title text,
  Author text,
  Date published integer);""")

cursor.execute("""INSERT INTO books(id,Title,Author,Date published)
 Values("1","De profundis",oscar Wilde,1905)""")
db.commit()

cursor.execute("""INSERT INTO books(id,Title,Author,Date published)
 Values("2","harry potter and chamber of secrets","J.K.Rowling","1998")""")
db.commit()

cursor.execute("""INSERT INTO books(id,Title,Author,Date published)
 Values("3","harry potter and chamber of secrets","J.K.Rowling","1998")""")
db.commit()

cursor.execute("""INSERT INTO  book(id,Title,Author,date published)
  VALUES("4","Lyrebird","ceccelia ahern,"2017")""")
db.commit()

cursor.execute("""INSERT INTO  book(id,Title,Author,date published)
  VALUES("5","Murder on the Orient Express","Agatha christie,"1934")""")
db.commit()

cursor.execute("""INSERT INTO  book(id,Title,Author,date published)
  VALUES("6","Perfect","ceccelia ahern,"2017")""")
db.commit()

cursor.execute("""INSERT INTO  book(id,Title,Author,date published)
  VALUES("7","The Marble Collector,"ceccelia ahern,"2016")""")
db.commit()

cursor.execute("""INSERT INTO  book(id,Title,Author,date published)
  VALUES("8","The murder on the links","Agatha Christie","1923")""")
db.commit()

cursor.execute("""INSERT INTO  book(id,Title,Author,date published)
  VALUES("9","The picture of dorian gray","Oscar Wilde","1890")""")
db.commit()

cursor.execute("""INSERT INTO  book(id,Title,Author,date published)
  VALUES("10","The secret adversary","Agatha Christie","1921")""")
db.commit()

cursor.execute("""INSERT INTO  book(id,Title,Author,date published)
  VALUES("11","The seven dials mystery","Agatha Christie","1929")""")
db.commit()

cursor.execute("""INSERT INTO  book(id,Title,Author,date published)
  VALUES("12","The year i met you","Cecelia Ahern","2014")""")
db.commit()
db.close()

#question 4
with sqlite3.connect ("bookinfo.db") as db:
    cursor = db.cursor()
    
cursor.execute("SELECT * FROM Author")
for x in cursor.fetchall():
    print (x)
cursor.execute("SELECT * FROM Place of birth")
for x in cursor.fetchall():
    print (x)
DOB =input("Enter place of birth: ")
cursor.execute("SELECT books.title,books.autho, books.date  published * FROM bookinfo WHERE place of birth = {DOB}")
for x in cursor.fetchall():
    print (x)
j