def teams_tied():
    import csv
    file=open("matches.csv",'r')
    reader=csv.reader(file)
    next(reader)
    tied_teams=[]
    for line in reader:
        result=line[8]
        team1=line[4]
        team2=line[5]
        if result=='tie':
            if team1 not in tied_teams:
                tied_teams.append(team1)
            if team2 not in tied_teams:
                tied_teams.append(team2)
    print("Teams that have tied matches are:")
    for team in tied_teams:
        print(team)
    file.close()
teams_tied()