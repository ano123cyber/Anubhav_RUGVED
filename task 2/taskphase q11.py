def sixcount():
    import csv
    file=open("deliveries.csv",'r')
    reader=csv.reader(file)
    next(reader)
    c=0
    for line in reader:
        six=line[15]
        if six=='6':
            c+=1
    print("Total number of sixes in the dataset:",c)
    file.close()
sixcount()
        