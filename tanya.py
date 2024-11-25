import argparse

def medals(team, year):
    medals_list = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
    file = "athlete_events.tsv"
    with open(file, "r", encoding='UTF-8') as file:
        header = file.readline().rstrip('\n').split('\t')
        year = header.index("Year")
        team = header.index("Team")
        noc = header.index("NOC")
        name = header.index("Name")
        event = header.index("Event")
        medal = header.index("Medal")

        for line in file:
            row = line.rstrip('\n').split('\t')
            if (row[team]==team or row[noc]==team) and row[year]==year and row[medal] != "NA":
                name, event, medal = row[name], row[event], row[medal]
                if medal in medals_list:
                    medals_list[medal] +=1

    print(f"Gold: {medals_list['Gold']}")
    print(f"Silver: {medals_list['Silver']}")
    print(f"Bronze: {medals_list['Bronze']}")
