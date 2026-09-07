def runs():
    import csv
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    next(reader)
    dict={}
    for line in reader:
        season=line[1]
        runs1=line[11]
        if season in dict:
            dict[season]=dict[season]+int(runs1)
        else:
            dict[season]=int(runs1)
    for season in dict:
        print("Season:",season,"\nTotal runs:",dict[season])
    file.close()
runs()