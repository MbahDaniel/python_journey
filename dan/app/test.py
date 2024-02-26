my_contacts = [{"name":"name of person 1","phone_number": "090876543555","id":1},{"name":" What your name","phone_number":"090878456378","id": 2}]

number = input("Enter Your phone number")
for i in my_contacts:
 if i["phone_number"] == number:
   print (number)