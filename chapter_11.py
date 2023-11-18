new_list = ["me", "you", "them"]
# new_list[0] = "them"


names_ofcountries_tuple =("uk","usa","nigeria","denmark","spain" )
print(f"{names_ofcountries_tuple}")
selected_country = input("enter one of the countries above ")
print(f"position of {selected_country} is{names_ofcountries_tuple.index}")

#question 2
names_ofcountries_tuple =("uk","usa","nigeria","denmark","spain" )
print(f"{names_ofcountries_tuple}")
selected_country = input("enter one of the countries above ")
print(f"position of {selected_country} is{names_ofcountries_tuple.index}")
numofanother_country = int(input("enter a number from 0 to 4"))
print(names_ofcountries_tuple[numofanother_country])

#question 3
sport1_tuple =("volleyball","basketball")
sport1_tuple.append(input("entervyour favourite sport: "))
sport1_tuple.sort()
print(sport1_tuple)

#question 4
subject_list = ["mathematics","english","physics","biology","chemistry","geography"]
dislike = input("enter a subject from the list for the subject you dislike: ")
remove = subject_list.index(dislike)
del subject_list[dislike]
print(f"{subject_list}")

#question 5
favourite_food = {}
food1 = input("enter a food you like: ")
favourite_food [1] = food1
food2 = input("enter a food you like: ")
favourite_food [2] = food2
food3 = input("enter a food you like: ")
favourite_food [3] = food3
food4 = input("enter a food you like: ")
favourite_food [4] = food4
dislike = int(input("enter a food you dont like: "))
del favourite_food [dislike]
print(sorted(favourite_food.value))

#Question 6
colors = ["green","orange","purple","yellow","black","red","blue","brown","pink","grey"]
starting_color = int(input("enter a color from 0 to 4"))
ending_color = int(input("enter a color from 5 to 9"))
print(colors.index[starting_color:ending_color])

#question 7
digit_list = ["787","564","678","789"]
print(digit_list)
for i in digit_list:
    print(i)
select = int(input("enter a number from"),digit_list)
if select in digit_list:
    print(select,"is in  the position",digit_list.index[select])
else:
   print("that is not in the list: ")

#question 8
name1 = input("enter a name: ")
name2 = input("enter a name: ")
name3 = input("enter a name: ")
party = ["name1","name2","name3"]
another_name = input("do you want to add another name","yes/no")
while party == "yes":
   print("This is the new list of names in the party",party.append[another_name])
another_name = input("do you want to add another name","yes/no")
print("This is the total of people you invited for the party",len(party))

#question 9
name1 = input("enter a name: ")
name2 = input("enter a name: ")
name3 = input("enter a name: ")
party = ["name1","name2","name3"]
another_name = input("do you want to add another name","yes/no")
while party == "yes":
   print("This is the new list of names in the party",party.append[another_name])
another_name = input("do you want to add another name","yes/no")
print("This is the total of people you invited for the party",len(party))
print(party)
another_name2 = input("enter any name on the list")
print(another_name2,"is in the position",party.index[another_name2])
stillcome = input("Do you still want them to come(yes/no): ")
if stillcome =="no":
   party.remove(another_name2)
print(party)

#question 10
tv_programmes = ["oga amos","sabinwa","turtle ninja","fantastic four"]
for i in tv_programmes:
   print(i)
another_programme = input("enter another show: ")
position = int(input("enter a position to input the next show: "))
print(tv_programmes.insert(position,another_programme))

#question 11
nums = []
total = 0
while total <3:
   add_num = int(input("enter a number: "))
   nums.append[add_num]
   print(nums)
ask = input("do you stll  like the last number you entered (yes/no): ")
if ask == "no":
  print(nums.remove(ask))