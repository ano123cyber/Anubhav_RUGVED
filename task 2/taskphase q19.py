def toss_decisions():
    import csv
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    next(reader)
    dict1={}
    for line in reader:
        season=line[1]
        toss_decision=line[7]
        if season in dict1:
            current_count=[]
            current_count=dict1[season]
            if toss_decision=='field':
                current_count[0]+=1
            if toss_decision=='bat':
                current_count[1]+=1
        else:
            if toss_decision=='field':
                current_count=[1,0]
            if toss_decision=='bat':
                current_count=[0,1]
        dict1[season]=current_count
    for season in dict1:
        current_count=dict1[season]
        print(season,"\nTotal no of 'field' choices:",current_count[0])
        print("Total no of 'bat' choices:",current_count[1])
    file.close()
toss_decisions()
