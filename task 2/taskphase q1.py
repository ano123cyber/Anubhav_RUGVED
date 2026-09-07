def no_matches():
    import csv
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    c=0
    next(reader)
    for line in reader:
        season=line[1]
        if season=='2008':
            c=c+1
    print("Number of matches held in 2008:",c)
    file.close()
no_matches()

