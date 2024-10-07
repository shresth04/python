#Dictionary can store the data in key value  pair
#e.g. name : Shresth
# order paprintir
# No duplicate
# Changeable
# syntax :- myinfo  = { "name" : "Shresth",
#                       "email": "s@wgmail.com",
#                     "mobile" : "9283632983",
#                        "age" : " 21"}
# program to add three names in a list
# list = []
# list.append("naman")
# list.append("shresth")
# list.append("rahul")
# list.insert(1,"pawan")
# list.append("sam")
# print(list)

myinfo = { "name" : "shresth",
           "email" : " s@gmail.com",
           "mobile" : " 989988364",
           "age" : " 19"}
#to access specific data from a dictionary.
print("My name is : ",myinfo["name"])
print("My email is : ",myinfo["email"])
print("My mobile no is : ",myinfo["mobile"])
print("My age is :",myinfo["age"])

#To access the complete dictionary key value
for key in myinfo.values():
    print(key)
myinfo["name"]="manan"
myinfo["age"]="22"
myinfo["email"]="manan@gmail.com"
myinfo["mobile"]="989376470"
(myinfo)
    
    #To add college name 
myinfo.update({"Gender" :"Male"})
myinfo.update({"college name ": "ITS ghaziabad"})
print(myinfo)

#for delete the data using pop function
myinfo.pop("Gender")
print(myinfo)

