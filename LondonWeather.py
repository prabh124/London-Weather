#Command used to read the text file and print the line of the hotel
def getLines(x):
    commandFile = open('London Temperature.txt', 'r') 
    job = commandFile.readlines()
    return job[x]

def numOfLines():
    with open('London Temperature.txt') as r:
        lines = 0
        for line in r:
            lines += 1
    return lines

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

def getMinTemp(maxLines, min):
    for i in range(maxLines):

        for j in range(1, 13):

            lineInfo = getLines(i)
            lineInfo = lineInfo.split(',')

            if float(lineInfo[j]) < float(min):

                min = lineInfo[j]
                year = lineInfo[0]
                monthNum = j
    month = checkMonth(monthNum)
    return min, year, month      

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

def searchYear(maxLines, year):
    sum = 0
    for i in range(maxLines):

        lineInfo = getLines(i)
        lineInfo = lineInfo.split(',')
        if int(lineInfo[0]) == int(year):
            for j in range(1, 13):
                sum += float(lineInfo[j])
    mean = sum / 12
    mean = round(mean, 2)
    return mean
                
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

year = input("What year would you like to find the mean temperature of? ")

mean = searchYear(maxLines, year)

if mean > 0:
    print("The mean temperature for the year", year, "is:", mean, "degrees\n")

else:
    print("The mean temperature for the year", year, "is unavailable!\n")
