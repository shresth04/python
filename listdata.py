#list is used to store multiple data
#list store different type of data like int string float 
#list can store the duplicate data

#create list and store your friends name
friendsName = ["ivan","shresth","shyam","ram","lucky",24,22,23,26,19]

#to access the data from list
#to get the single data from list -> listvariableName[indexNo]
print(friendsName[3])


    #operation on list ->
friendsName.append("Rahul")
    #insert will add the data based on the index no
friendsName.insert(0,"Piyush")
friendsName.insert(3,"Naman")

#to remove the data from list
friendsName.remove("Piyush")
friendsName.remove("ivan")

#to remove the data from list using pop
friendsName.pop(0)
 
    #to print the complete lsit

for name in friendsName:
 print(name)
 
 #to print the complete list

for name in friendsName[1:3]:
    print(name)

print(friendsName)
for name in friendsName[:]:
 #print(name) 
 
 friendsName.sort
 friendsName[3] = "Ram Sharma"

for name in friendsName[:]:
 print(name)