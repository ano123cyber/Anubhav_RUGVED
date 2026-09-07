def wickets():
    import csv
    file=open("deliveries.csv",'r')
    reader=csv.reader(file)
    next(reader)
    dict={}
    for line in reader:
        bowler=line[8]
        player_dismissed=line[19]
        dismissal_kind=line[20]
        if player_dismissed!='' and dismissal_kind!='run out':
            if bowler in dict:
                dict[bowler]+=1
            else:
                dict[bowler]=1
    for bowler in dict:
        print(bowler,":",dict[bowler],"wickets")
    file.close()
wickets()