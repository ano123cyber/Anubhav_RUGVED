def teamwon():
    import csv
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    next(reader)
    dict1={}
    list1=[]
    for line in reader:
        res=line[11]
        team=line[10]
        if team in dict1:
            dict1[team]+=1
        else:
            dict1[team]=1
    for team in dict1:
        list1.append(dict1[team])
    max1=max(list1)
    min1=min(list1)
    for team in dict1:
        if dict1[team]==max1:
            print("Team with maximum wins is:",team)
        if dict1[team]==min1:
            print("Team with minimum wins is:",team)
    file.close()
teamwon()
