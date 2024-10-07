# To create a class
# class<ClassName>:
# Class name always should be in capital letter

# class Shresth:
#   print("my name is Shresth")

# class Student:
#     name="shresth"

# stu:Student = Student()
# print(stu.name)

# class with object && function
# class Student:
#     name="Shresth"
#     email="shresth6378@gmail.com"

#     def findMyAge(this,cY,bY):
#         ageInYear =  cY-bY
#         print(ageInYear)
# stu:Student = Student()
# stu.findMyAge(2024, 2006)

#     def monthlyPocketMoney(this,WeeklyMoney):
#         totalMoney = WeeklyMoney*4
#         print("My Pocket Money",totalMoney)
        
# stu:Student=Student()
# stu.monthlyPocketMoney(int(input("Enter Weekly Money")))

class Car:
        carName="Scorpio"
        model="2024"
        gear="7"
        firstGearspeed="50km\h"
        def findTopSpeed(this,top):
            topSpeed=50*top
            print("Top Speed", topSpeed)
stu:Car = Car()
stu.findTopSpeed(int(input("enter your gear no")))     
               