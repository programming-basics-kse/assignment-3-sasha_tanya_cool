import argparse

def top_players(file, top_n, gender, age_kategor=None, weight_kategor=None, height_kategor=None):
    age_ranges = {
        "1":(18, 25),
        "2":(25, 35),
        "3":(35, 50),
        "4":(50, float("inf")),
    }

    weight_ranges= {
        "1": (40, 60),
        "2": (60, 80),
        "3": (80, 100),
        "4": (100, float("inf")),
    }
    height_ranges = {
        "1": (150, 175),
        "2": (175, 190),
        "3": (190, 200),
        "4": (200, float("inf")),
    }

    players ={}

    with open(file, "r", encoding='UTF-8') as file:
        header = file.readline().rstrip('\n').split('\t')
        NAME = header.index("Name")
        SEX = header.index("Sex")
        AGE = header.index("Age")
        WEIGHT = header.index("Weight")
        HEIGHT = header.index("Height")
        MEDAL = header.index("Medal")

    top_players = sorted(players.items(), key=lambda  x: x[1], reverse=True)[:top_n]


    for line in file:
        row = line.rstrip("\n").split("\t")
        if row[SEX] != gender:
            continue

            age = int(row[AGE]) if row[AGE].isdigit() else None
            weight = float(row[WEIGHT]) if row[WEIGHT].replace(".", "").isdigit() else None
            height = float(row[HEIGHT]) if row[HEIGHT].replace(".", "").isdigit() else None

            if age_kategor and (age is None or not (age_ranges[age_kategor][0] <= age < age_ranges[age_kategor][1])):
                continue

            if weight_kategor and (weight is None or not (weight_ranges[weight_kategor][0] <= weight < weight_ranges[weight_kategor][1])):
                continue

            if height_kategor and (height is None or not (height_ranges[height_kategor][0] <= height < height_ranges[height_kategor][1])):
                continue

            if row[MEDAL] != "NA":
                medal_score = {"Gold": 5, "Silver": 3, "Bronze": 1}[row[MEDAL]]
                players[row[NAME]] = players.get(row[NAME], 0) + medal_score
parser.add_argument("-top", nargs=2, help="Find top players by criteria")
parser.add_argument("-a", help="Age group (1-4)")
parser.add_argument("-w", help="Weight group (1-4)")
parser.add_argument("-height", help="Height group (1-4)")

if args.top:
    top_n = int(args.top[0])
    gender = args.top[1]
    age_kategor = args.a
    weight_kategor = args.w
    height_kategor = args.height  # Заміна args.h на args.height
    top_players(file, top_n, gender, age_kategor, weight_kategor, height_kategor)


