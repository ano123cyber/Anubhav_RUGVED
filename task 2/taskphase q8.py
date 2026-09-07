def stats():
    import csv
    import statistics
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    next(reader)
    list1=[]
    for line in reader:
        res=line[11]
        list1.append(int(line[11]))
    mean=statistics.mean(list1)
    median=statistics.median(list1) 
    std_dev=statistics.stdev(list1)
    print("Mean of total scores is:",mean)  
    print("Median of total scores is:",median)
    print("Standard deviation of total scores is:",std_dev)
    file.close()
stats()
