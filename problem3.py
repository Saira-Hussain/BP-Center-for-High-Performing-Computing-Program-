# user input values
value1= input("Enter x-axis value: ")
value2= input("Enter y-axis value: ")
value3= input("Enter distance: ")
x= int(value1)
y= int(value2)
d= float(value3)
result = 0
# calculate the total number of nodes using an algorithm
if (((x>=0) and (y>0)) or (((x>0) and (y>=0)))):
        result =((x//d)+1)*((y//d)+1)
print (“Total number of nodes:” str(result))

#import csv and convert knots to mph- add to data list
import csv
data=[]
with open('WeatherForecast.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvfile:
        if "Good" in row:
            data.append(24.166)
        else:
            data.append(19.563)

#create an hour list with the number of hours it take to travel from node to node
hours=[]
for x in data:
    hours.append(d/x)

#add extra bad weather days if needed
if (result>len(hours)):
    while(result>len(hours)):
        data.append(19.563)
        hours.append(d/19.563)
#calculating the total time for all nodes
count=0
totalTime=0
for h in hours:
    while count<=(result-1):
        totalTime=totalTime+h+0.5
        count=count+1
totalTime=totalTime+0.5
#figure out how many days
days=totalTime/24
print("Days: " + str(days))
print("Cost: " + str(days) + " million dollars")
