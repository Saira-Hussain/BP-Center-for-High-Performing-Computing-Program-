mainlist = []

# import the csv file
import pandas as pd
data = pd.read_csv ("Downloads/TapeData.csv")   

titlelist = data["Tape ID"]
datalist = data["Data Size "]

# save the values in the csv as a string in the mainlist
for k, value in enumerate(datalist):
    mainlist.append(" ")
    mainlist[len(mainlist)-1] = str(titlelist[k] + " " + datalist[k])

# sort the list
newList = [] 
minimum = 0
lengthList = len(mainlist)



# sort the list
for j in range (lengthList, 0, -1):
    minimum = 0
    for i, value in enumerate(mainlist):
        # set the tempi and tempMin values
        # remove the Title from the beginning of the string
        tempi = value
        tempi = tempi[7:len(tempi)]
        tempMin = mainlist[minimum]
        tempMin = tempMin[7:len(tempMin)]
        # translate to the same data type
        if "TB" in tempi and "TB" in tempMin:
            tempi = float(tempi[0:len(tempi)-3])*1000
            tempMin = float(tempMin[0:len(tempMin)-3])*1000
        elif "TB" in tempi:
            tempi = float(tempi[0:len(tempi)-3])*1000
            tempMin = float(tempMin[0:len(tempMin)-3])
        elif "TB" in tempMin:
            tempi = float(tempi[0:len(tempi)-3])
            tempMin = float(tempMin[0:len(tempMin)-3])*1000
        else:
            tempi = float(tempi[0:len(tempi)-3])
            tempMin = float(tempMin[0:len(tempMin)-3])
        # check if the selected value is less than the current minimum value
        if tempi < tempMin:
            minimum = i
    # after all values checked, add the minimum value from the mainlist to the newlist
    # delete the minimum value from the list
    newList.append(mainlist[minimum])
    del mainlist[minimum]
    #repeat the for loop for all the values in the data set

 
    


# write in the list to the csv file
rowTitle = ["Tape ID" , "Data Size "]
rowInfo = []
tempList = []
title = ""
data = ""

for m, value in enumerate(newList):
    title = newList[m]
    title = title[0:6]
    tempList.append(title)

    data = newList[m]
    data = data[7:len(data)]
    tempList.append(data)

    rowInfo.append(tempList)
    tempList = []

with open("TapeData.csv", 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the fields 
    csvwriter.writerow(rowTitle)
    # writing the data rows 
    csvwriter.writerows(rowInfo)

