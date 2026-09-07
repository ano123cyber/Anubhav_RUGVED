def venuedetails():
    import csv
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    next(reader)
    list1=[]
    dict1={}
    for line in reader:
        res=line[11]
        venue=line[14]
        if not res.isdigit():
            continue
        if int(res)==0:
            continue
        list1.append(int(line[11]))
        if venue in dict1:
            dict1[venue].append(int(line[11]))
        else:
            dict1[venue] = [int(line[11])]
    max1=max(list1)
    min1=min(list1)
    for venue in dict1:
        if max1 in dict1[venue]:
            print("Venue with maximum score is:",venue,"\nMargin:",max1)
        if min1 in dict1[venue]:
            print("Venue with minimum score is:",venue,"\nMargin:",min1)
    file.close()
venuedetails()