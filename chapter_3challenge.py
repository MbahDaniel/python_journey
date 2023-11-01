#question 1
name = input("enter your first name: ")
lenth = len(name)
print(lenth)

#question 2
name1 = input("enter your first name: ")
name2 = input("enter  your  surname:  ")
print (F"{name1} {name2}: ")

#question 3
nam = input("enter your first name: ").lower()
name = input("surname: ").lower()
nam.title()
name.title()
print(f"{nam} {name}: ")

#question 4
rhyme = input("first line of nusery rhyme: ")
lenth = len(rhyme)
print(lenth)
start = input("starting number: ")
last = input("ending number: ")
print(f"{start} {last}: ")

#question 5
word = input("enter any word: ")
print(word.upper())

#question 6
fname = input("enter your first name: ")
lenth = len(fname)
if lenth < 5:
    surname =input("enter your surname: ")
    print(f"{fname} {surname}".upper())
elif fname >= 5:
    print(fname.lower())
else:
    print("continue: ".upper())

# question 7
word = input("Enter A Word: ")
vowels = ["a", "e", "i", "o", "u"]

if word[0] in vowels:
    print(f"{word[1:]}way")
else:
    print(f"{word[1:]}{word[0]}ay")


