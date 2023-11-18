#Question 1
first_name = input("enter a name: ")
print("number of characters",len(first_name))
surname = input("enter a name: ")
print("number of characters",len(surname))
name = first_name +" "+ surname
print("this is your full name",name)
print(len(name))

#Question 2
fav_school_subject = input("Enter your favourite school subject: ")
for i in fav_school_subject:
    print(i)

#Question 3
poem = ("betty butter bought some butter")
print(poem)
start_point = input("enter a start point: ")
end_point = input("enter a number: ")
print(poem[start_point:end_point])

#Question 4
word = input("enter a word in upper case: ")
tryagain = "false"
while tryagain == "false":
    if word.islower():
       print("tryagain")
    else:
       print("thanks")
       word = input("enter a word in upper case: ")

#question 5
postcode = input("enter your postcode: ")
code = postcode[0:2]
print(code.upper())

#question 6
name = input("Enter a name: ").lower()#ask the user to enter a name
for i in name:
    if i == "a " or "e" or "i" or "o" or "u":



#question 7
word1 = input("enter a name: ").upper()
word2 = input("enter a name: ")
if word1 ==  word2:
    print("thank you")
elif word1 == word2.lower():
    print("they must be in the same case: ")
else:
    print("incorrect")

#question 8
enter =  input("enter a word: ")
length = len(enter)
next = 1
for i in enter:
    print(enter[length - next])
    next = next + 1
    











