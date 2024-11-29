import argparse

def write_output(output_file, summary):
    with open(output_file, "a", encoding='UTF-8') as file:
        file.write(summary)

def medals(team, year, output_file=None):
    medals_list = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
    file = "athlete_events.tsv"

    found_team = False
    found_year = False
    found_medals = False

    with open(file, "r", encoding='UTF-8') as file:
        header = file.readline().rstrip('\n').split('\t')
        YEAR = header.index("Year")
        TEAM = header.index("Team")
        NOC = header.index("NOC")
        NAME = header.index("Name")
        EVENT = header.index("Event")
        MEDAL = header.index("Medal")

        counter=0
        for line in file:
            row = line.rstrip('\n').split('\t')
            if (row[TEAM] == team or row[NOC] == team):
                found_team = True
            if row[YEAR]==year:
                found_year = True

            if (row[TEAM]==team or row[NOC]==team) and row[YEAR]==year and row[MEDAL] != "NA":
                found_medals = True
                name, event, medal = row[NAME], row[EVENT], row[MEDAL]
                medals_list[medal] +=1

                if counter < 10:
                    print(f"{name}; {event}: {medal}")
                    counter += 1

                if output_file and counter <=10:
                    write_output(output_file, f"{name}; {event}: {medal}\n")
        if not found_team:
            print(f"!!ERROR. WE CAN NOT FOUND {team}!!")
        elif not found_year:
            print(f"!!THERE WERE NO OLYMPICS IN {year}!!")
        elif not found_medals:
            print(f"!!NO MEDALS FOR THE {team} in {year} FOUND!!")
        else:
            summary =(
                f"Gold: {medals_list['Gold']}\n"
                f"Silver: {medals_list['Silver']}\n"
                f"Bronze: {medals_list['Bronze']}\n"
            )
            print(summary)

        if output_file:
            write_output(output_file, summary)
            
parser = argparse.ArgumentParser(description="Olympic medals")
file = "athlete_events.tsv"

parser.add_argument("-medals", nargs=2, help="Country of team and year of Olympics")
args = parser.parse_args()

if args.medals:
    team, year = args.medals
    output_file = args.output
    medals(team, year, output_file)
