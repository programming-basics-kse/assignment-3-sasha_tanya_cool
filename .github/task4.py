def find_best_year(data, country):
    best_year = None
    max_medals = 0
    for year in set(row['Year'] for row in data if row['Team'] == country):
        medals = medals(data, country, year)
        total_medals = sum(medals.values())
        if total_medals > max_medals:
            max_medals = total_medals
            best_year = year
    return best_year
def find_worst_year(data, country):
    worst_year = None
    min_medals = 0
    for year in set(row['Year'] for row in data if row['Team'] == country):
        medals = medals(data, country, year)
        total_medals = sum(medals.values())
        if total_medals < min_medals:
            min_medals = total_medals
            worst_year = year
    return worst_year
