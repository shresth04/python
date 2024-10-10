import numpy as np

#assign array in numpy
myData = np.array([1,2,3,4])
print(myData)
print(type(myData))

#update the data in array
myData[0] = 9
print(myData)
myData[1] = 10
myData[2] = 11
myData[3] = 12
print(myData)

#by ussing for loop
a = 9
for data in range(0,4):
    myData[data] = a + data
b = 0
while b < 4:
    myData[b] = a + b
    b = b+1
print(myData)

#access the data from numpy array
for data in range(0,4):
    print(myData[data])
    
myFriends = np.array(["ivan","rahul","ram","rajat"])
for name in myFriends:
    print(name)
    myFriends.sort()
    print(myFriends)

x = 3
while x >= 0:
    print(myFriends[x])
    x = x - 1