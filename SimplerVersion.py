def loadData(filename='LondonTemperature.csv'):

    import re

    file = open(filename, 'r')
    records = []

    for r in file.readlines():
        r = re.sub(r'[^a-zA-Z0-9.,-]+', '', r)
        records.append(r.split(','))
        
    return records

records = loadData()

def coldestMonth(records):

    coldest = 100
    for record in records:
          
        year = int(record[0])
        jan = float(record[1])
        feb = float(record[2])
        mar = float(record[3])
        apr = float(record[4])
        may = float(record[5])
        jun = float(record[6])
        jul = float(record[7])
        aug = float(record[8])
        sep = float(record[9])
        oct = float(record[10])
        nov = float(record[11])
        dec = float(record[12])

        currentColdest = min(jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec)

        if currentColdest < coldest:
            coldest = currentColdest

        if jan is coldest:
            coldestMonth = 'January'
        elif feb is coldest:
            coldestMonth = 'February'
        elif mar is coldest:
            coldestMonth = 'March'
        elif apr is coldest:
            coldestMonth = 'April'
        elif may is coldest:
            coldestMonth = 'May'
        elif jun is coldest:
            coldestMonth = 'June'
        elif jul is coldest:
            coldestMonth = 'July'
        elif aug is coldest:
            coldestMonth = 'August'
        elif sep is coldest:
            coldestMonth = 'September'
        elif oct is coldest:
            coldestMonth = 'October'
        elif nov is coldest:
            coldestMonth = 'November'
        elif dec is coldest:
            coldestMonth = 'December'
    print("The coldest month is", coldestMonth, "and its temperature was:", coldest, "degrees!\n")

def hottestMonth(records):

    hottest = -100
    for record in records:
        
        year = int(record[0])
        jan = float(record[1])
        feb = float(record[2])
        mar = float(record[3])
        apr = float(record[4])
        may = float(record[5])
        jun = float(record[6])
        jul = float(record[7])
        aug = float(record[8])
        sep = float(record[9])
        oct = float(record[10])
        nov = float(record[11])
        dec = float(record[12])

        currentHottest = max(jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec)

        if currentHottest > hottest:
            hottest = currentHottest

        if jan is hottest:
            hottestMonth = 'January'
        elif feb is hottest:
            hottestMonth = 'February'
        elif mar is hottest:
            hottestMonth = 'March'
        elif apr is hottest:
            hottestMonth = 'April'
        elif may is hottest:
            hottestMonth = 'May'
        elif jun is hottest:
            hottestMonth = 'June'
        elif jul is hottest:
            hottestMonth = 'July'
        elif aug is hottest:
            hottestMonth = 'August'
        elif sep is hottest:
            hottestMonth = 'September'
        elif oct is hottest:
            hottestMonth = 'October'
        elif nov is hottest:
            hottestMonth = 'November'
        elif dec is hottest:
            hottestMonth = 'December'
    print("The hottest month is", hottestMonth, "and its temperature was:", hottest, "degrees!\n")
    

def findMean(year, records):
    sum = 0
    for record in records:
        searchYear = record[0]
        if int(year) == int(searchYear):
            for i in range(1, 13):
                sum += float(record[i])
    if sum is 0:
        print("\nERROR: No year found!\n")
    else:
        mean = sum / 12
        mean = round(mean, 2)
        print("The mean temperature of the year " + year, "was: " + str(mean), "degrees!")

    


       

coldestMonth(records)
hottestMonth(records)
year = input("What year would you like to search for? ")
findMean(year, records)



