def matches():
    import csv
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    next(reader)
    dict={}
    for line in reader:
        season=line[1]
        if season in dict:
            dict[season]+=1
        else:
            dict[season]=1
    for season in dict:
        print("Season:",season,"\nTotal matches:",dict[season])
    file.close()
matches()