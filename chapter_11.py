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
favourite_foods = input("enter four of your favourite food: ")



