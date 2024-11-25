import argparse

def medals(team, year):
    medals_list = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
    file = "athlete_events.tsv"
    with open(file, "r", encoding='UTF-8') as file:
        header = file.readline().rstrip('\n').split('\t')
        YEAR = header.index("Year")
        TEAM = header.index("Team")
        NOC = header.index("NOC")
        NAME = header.index("Name")
        EVENT = header.index("Event")
        MEDAL = header.index("Medal")

        for line in file:
            row = line.rstrip('\n').split('\t')
            if (row[TEAM]==team or row[NOC]==team) and row[YEAR]==year and row[MEDAL] != "NA":
                name, event, medal = row[NAME], row[EVENT], row[MEDAL]
                medals_list[medal] +=1

        print(f"Gold: {medals_list['Gold']}")
        print(f"Silver: {medals_list['Silver']}")
        print(f"Bronze: {medals_list['Bronze']}")

parser = argparse.ArgumentParser(description="Olympic medals")
parser.add_argument("-medals", nargs=2, required=True, help="Country of team and year of Olympics")

args = parser.parse_args()
team, year = args.medals

medals(team, year)