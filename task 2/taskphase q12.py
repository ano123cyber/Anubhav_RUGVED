def avg():
    import csv
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    next(reader)
    dict1={}
    dict2={}
    for line in reader:
        city1=line[2]
        runs=line[11]
        if not runs.isdigit():
            continue
        if city1 in dict1:
            dict1[city1]+=int(runs)
            dict2[city1]+=1
        else:
            dict1[city1]=int(runs)
            dict2[city1]=1
    for city1 in dict1:
        average_runs=int(dict1[city1]/dict2[city1])
        print("Average runs scored in",city1,"is:",average_runs)
    file.close()
avg()