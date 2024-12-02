import argparse

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

parser.add_argument("-overall", nargs="+", help = "Write all of countries that you want to check" )
args = parser.parse_args()

if args.overall:
    countries = args.overall
    overall(file, countries)
