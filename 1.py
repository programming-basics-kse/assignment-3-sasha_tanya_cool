import argparse
from idlelib.iomenu import encoding


def total(year):
    file = "athlete_events.tsv"
    medals_by_country = {}

    with open(file, "r", encoding="utf-8") as file:
        header = file.readline().rstrip('\n').split('\t')
        YEAR = header.index("Year")
        TEAM = header.index("Team")
        MEDAL = header.index("Medal")

        found_year = False
        for line in file:
            row = line.rstrip('\n').split('\t')
            if row[YEAR] == year:
                found_year = True
                if row[MEDAL] != "NA":
                    country = row[TEAM]
                    medal = row[MEDAL]
                    if country not in medals_by_country:
                        medals_by_country[country] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
                    medals_by_country[country][medal] += 1

        if not found_year:
            print(f"!!THERE WERE NO OLYMPICS IN {year}")
        else:
            for country, counts in medals_by_country.items():
                print(f"{country} - Gold: {counts['Gold']}, Silver: {counts['Silver']}, Bronze: {counts['Bronze']}"
parser=argparse.ArgumentParser(description="Olympic medals,")
parser.add_argument("-medals", nargs=2, help="Country of team and year of Olympics")
parser.add_argument("-output", help = "Name of file where summary will be saved")
parser.add_argument("-overall", nargs="+", help = "Write all of countries that you want to check" )
parser.add_argument("-total", type=str, help="Year for total medal count")

args = parser.parse_args()
elif args.total:
    total(args.total)