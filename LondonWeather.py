#Command used to read the text file and return line info with the corresponding line number
def getLines(x):
    commandFile = open('London Temperature.txt', 'r') 
    lineInfo = commandFile.readlines()
    return lineInfo[x]

#count the number of lines inside the file, this will be used for later functions
def numOfLines():
    with open('London Temperature.txt') as r:
        lines = 0
        for line in r:
            lines += 1
    return lines

#Helper function to clear clutter in the main. Used to identify what index the month is attached to
def checkMonth(monthNum):
    if monthNum is 1:
        return 'January'
    elif monthNum is 2:
        return 'February'
    elif monthNum is 3:
        return 'March'
    elif monthNum is 4:
        return 'April'
    elif monthNum is 5:
        return 'May'
    elif monthNum is 6:
        return 'June'
    elif monthNum is 7:
        return 'July'
    elif monthNum is 8:
        return 'August'
    elif monthNum is 9:
        return 'September'
    elif monthNum is 10:
        return 'October'
    elif monthNum is 11:
        return 'November'
    else:
        return 'December'

#Coldest temp function
def getMinTemp(maxLines, min):

    #Iterate through the text file until it reaches the last line
    for i in range(maxLines):

        #iterate through each index for the specified line
        for j in range(1, 13):

            #splitting the numbers everytime a comma is found, used to allow for indexing
            lineInfo = getLines(i)
            lineInfo = lineInfo.split(',')

            #if the number at the index of j is below the minimum (set to 100 to start with), then that becomes the new minimum
            if float(lineInfo[j]) < float(min):

                min = lineInfo[j]
                #Check the year of the lowest temp at the zeroth index
                year = lineInfo[0]
                #month number is equal to the index, then call the checkMonth helper function to attach a name to that index
                monthNum = j

    month = checkMonth(monthNum)
    return min, year, month      

#hottest temperature function, same steps as the coldest except it checks for indexes higher than the previous max
def getMaxTemp(maxLines, max):
    for i in range(maxLines):

        for j in range(1, 13):

            lineInfo = getLines(i)
            lineInfo = lineInfo.split(',')

            if float(lineInfo[j]) > float(max):

                max = lineInfo[j]
                year = lineInfo[0]
                monthNum = j

    month = checkMonth(monthNum)
    return max, year, month

#function to search for a certain year and pull the mean temperature of that year
def searchYear(maxLines, year):
    #declare sum to find the avg
    sum = 0

    #iterate through the file until the last line is reached
    for i in range(maxLines):

        #splitting numbers like before
        lineInfo = getLines(i)
        lineInfo = lineInfo.split(',')

        #if the zeroth index is equal to the year that is inputted, take the sum of the temperatures corresponding to that year
        if int(lineInfo[0]) == int(year):
            for j in range(1, 13):
                sum += float(lineInfo[j])
    #calculate meaning by taking the sum/amount of months (12)
    mean = sum / 12
    mean = round(mean, 2)
    return mean

#initializing variables  
maxLines = numOfLines()
minYear = 0
maxYear = 0
minMonth = 0
maxMonth = 0
min = 100.00
max = -100.00

min, minYear, minMonth = getMinTemp(maxLines, min)

max, maxYear, maxMonth = getMaxTemp(maxLines, max)

print("London weather temperature. \n")

print(minMonth, minYear, "was the coldest month on record with a mean temperature of: " + min, "degrees.\n")

print(maxMonth, maxYear, "was the hottest month on record with a mean temperature of: " + max, "degrees.\n")

#retrieve user input on what year to search for
year = input("What year would you like to find the mean temperature of? ")

mean = searchYear(maxLines, year)

#if the mean is zero or below, then print that the year inputted is unavailable in this dataset
if mean > 0:
    print("The mean temperature for the year", year, "is:", mean, "degrees\n")

else:
    print("The mean temperature for the year", year, "is unavailable!\n")
