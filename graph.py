import pandas
import matplotlib.pyplot as plt
import numpy as np

plt.title("My Academic Grades")
plt.xlabel("years")
plt.ylabel("Grades")
plt.grid()

# year = np.array([2005,2006,2007,2011])
# grade = np.array([54.05,71,69,76])
# plt.plot(year,grade)
# plt.show()

name=["python","java","c++","react"]
x= np.array([90,500,20,60])
plt.pie(x)
plt.show()