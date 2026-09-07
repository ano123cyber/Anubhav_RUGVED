def toss_decision():
    import csv
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    next(reader)
    dict1={}
    for line in reader:
        toss_winner=line[6]
        decision=line[7]
        if toss_winner in dict1:
            current_count=[]
            current_count=dict1[toss_winner]
            if decision=='field':
                current_count[0]+=1
            if decision=='bat':
                current_count[1]+=1
        else:
            if decision=='field':
                current_count=[1,0]
            if decision=='bat':
                current_count=[0,1]
        dict1[toss_winner]=current_count
    for toss_winner in dict1:
        current_count=dict1[toss_winner]
        print(toss_winner,"took",current_count[0],"times field and",current_count[1],"times bat")
    file.close()
toss_decision()
