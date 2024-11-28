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

def overall(file, countries):
    country_medals = {country: {'Gold': 0, 'Silver': 0, 'Bronze': 0, 'Years': {}} for country in countries}
    with open(file, "r", encoding='utf-8') as file:
        header = file.readline().rstrip('\n').split('\t')
        YEAR = header.index("Year")
        TEAM = header.index("Team")
        NOC = header.index("NOC")
        MEDAL = header.index("Medal")

        for line in file:
            row = line.rstrip('\n').split('\t')
            for country in countries:
                if (row[TEAM] == country or row[NOC] == country) and row[MEDAL] != 'NA':
                    medal = row[MEDAL]
                    year = row[YEAR]
                    country_medals[country][medal] += 1

                    if year not in country_medals[country]["Years"]:
                        country_medals[country]["Years"][year] = 0
                    country_medals[country]["Years"][year] += 1

    for country in countries:
        if country_medals[country]["Years"]:
            best_year = max(country_medals[country]["Years"], key=country_medals[country]["Years"].get)
            total_medals = sum(country_medals[country]["Years"].values())
            print(f"The best year for {country} was {best_year} when {country} won {country_medals[country]["Years"][best_year]} medals")
            print(
                f"Total medals for {country}: {total_medals} (Gold: {country_medals[country]['Gold']}, Silver: {country_medals[country]['Silver']}, Bronze: {country_medals[country]['Bronze']})\n"
            )
        else:
            print(f"No medals found for {country}")


parser = argparse.ArgumentParser(description="Olympic medals")
file = "athlete_events.tsv"


parser.add_argument("-medals", nargs=2, help="Country of team and year of Olympics")
parser.add_argument("-output", help = "Name of file where summary will be saved")
parser.add_argument("-overall", nargs="+", help = "Write all of countries that you want to check" )
args = parser.parse_args()


if args.medals:
    team, year = args.medals
    output_file = args.output
    medals(team, year, output_file)

elif args.overall:
    countries = args.overall
    overall(file, countries)

