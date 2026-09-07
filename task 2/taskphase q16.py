def batsmen():
    import csv
    file=open("deliveries.csv",'r')
    reader=csv.reader(file)
    next(reader)
    dict={}
    for line in reader:
        batsman=line[6]
        runs=line[15]
        if batsman in dict:
            dict[batsman]+=int(runs)
        else:
            dict[batsman]=int(runs)
    for i in range(10):
        max1=max(dict.values())
        for batsman in dict:
            if dict[batsman]==max1:
                print(batsman,"\nTotal runs:",max1)
                del dict[batsman]
                break
    file.close()
batsmen()

