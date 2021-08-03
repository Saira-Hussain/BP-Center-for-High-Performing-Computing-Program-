import numpy as np
import matplotlib.pyplot as plt

# user input values
value1= input("Enter x-axis value: ")
value2= input("Enter y-axis value: ")
value3= input("Enter distance: ")

x= int(value1)
y= int(value2)
d= float(value3)
result = 0

# calculate the total number of nodes using an algorithm
if (d>0):
    if (((x>=0) and (y>0)) or (((x>0) and (y>=0)))):
        total=((x//d)+1)*((y//d)+1)


# save the node coordinates in xList and yList

count = 0
xList = [0.]
while count < x:
    	xList.append(count)
count += d
    

count = 0
yList = [0.]
while count < y:
        	yList.append(count)
count += d



# create the combinations of x and y coordinates

for a in xList:
    for b in yList:
plt.scatter(a, b, label = "stars", color = "green", marker= "*", s=30)

# set up the plot
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Nodes Plot')

# show information
print("Nodes: " + str(result))
plt.show()



