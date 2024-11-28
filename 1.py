from builtins import print
from builtins import open
def total(year):
    file = "athlete_events.tsv"
    medals_by_country = {}

    with open(file, "r") as file:
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
            print(f"!!THERE WERE NO OLYMPICS IN {year}!!")
        else:
            for country, counts in medals_by_country.items():
                print(f"{country} - Gold: {counts['Gold']}, Silver: {counts['Silver']}, Bronze: {counts['Bronze']}")