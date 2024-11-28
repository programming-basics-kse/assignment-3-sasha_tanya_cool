def load_data(file):
    data = []
    with open(file, "r", encoding='UTF-8') as f:
        header = f.readline().rstrip('\n').split('\t')
        for line in f:
            row = line.rstrip('\n').split('\t')
            data.append(dict(zip(header, row)))
    return data

def find_best_year(data, country):
    best_year = None
    max_medals = 0
    for year in set(row['Year'] for row in data if row['Team'] == country):
        medals = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
        # Count medals for the given country and year
        for row in data:
            if row['Team'] == country and row['Year'] == year:
                medal = row['Medal'].capitalize()  # Ensure 'Medal' is capitalized
                if medal in medals:
                    medals[medal] += 1
        total_medals = sum(medals.values())
        if total_medals > max_medals:
            max_medals = total_medals
            best_year = year
    return best_year

def find_worst_year(data, country):
    worst_year = None
    min_medals = float('inf')
    for year in set(row['Year'] for row in data if row['Team'] == country):
        medals = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
        # Count medals for the given country and year
        for row in data:
            if row['Team'] == country and row['Year'] == year:
                medal = row['Medal'].capitalize()  # Ensure 'Medal' is capitalized
                if medal in medals:
                    medals[medal] += 1
        total_medals = sum(medals.values())
        if total_medals < min_medals:
            min_medals = total_medals
            worst_year = year
    return worst_year

def average_medals(data, country):
    total_medals = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
    years = set(row['Year'] for row in data if row['Team'] == country)
    for year in years:
        medals = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
        # Count medals for the given country and year
        for row in data:
            if row['Team'] == country and row['Year'] == year:
                medal = row['Medal'].capitalize()  # Ensure 'Medal' is capitalized
                if medal in medals:
                    medals[medal] += 1
        for medal_type, count in medals.items():
            total_medals[medal_type] += count
    if years:
        average_medals = {medal_type: count / len(years) for medal_type, count in total_medals.items()}
    else:
        average_medals = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
    return average_medals

def interactive_mode(file):
    data = load_data(file)
    while True:
        country = input("Enter country (or 'exit'): ")
        if country.lower() == 'exit':
            break
        best = find_best_year(data, country)
        worst = find_worst_year(data, country)
        avg_medals = average_medals(data, country)
        print(f"The best year for {country}: {best}")
        print(f"The worst year for {country}: {worst}")
        print(f"Average amount of medals: {avg_medals}")

parser = argparse.ArgumentParser(description="Olympic medals")
file = "athlete_events.tsv"


parser.add_argument("-medals", nargs=2, help="Country of team and year of Olympics")
parser.add_argument("-output", help = "Name of file where summary will be saved")
parser.add_argument("-overall", nargs="+", help = "Write all of countries that you want to check" )
parser.add_argument("-total", type=str, help="Year for total medal count")
parser.add_argument("-interactive", action="store_true", help="Interactive mode")

args = parser.parse_args()

if args.medals:
    team, year = args.medals
    output_file = args.output
    medals(team, year, output_file)

elif args.overall:
    countries = args.overall
    overall(file, countries)

elif args.total:
    total(args.total)

elif args.interactive:
    interactive_mode(file)