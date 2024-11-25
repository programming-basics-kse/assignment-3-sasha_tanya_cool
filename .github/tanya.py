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
