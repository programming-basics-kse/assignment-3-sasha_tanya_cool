
        for line in file:
            row = line.rstrip("\n").split("\t")
            if row[SEX] != gender:
                continue

            age = int(row[AGE]) if row[AGE].isdigit() else None
            weight = float(row[WEIGHT]) if row[WEIGHT].replace(".", "").isdigit() else None
            height = float(row[HEIGHT]) if row[HEIGHT].replace(".", "").isdigit() else None

        if age_group and (age is None or not (age_ranges[age_group][0] <= age < age_ranges[age_group][1])):
            continue

        if weight_group and (weight is None or not (weight_ranges[weight_group][0] <= weight < weight_ranges[weight_group][1])):
            continue

        if height_group and (height is None or not (height_ranges[height_group][0] <= height < height_ranges[height_group][1])):
            continue

        if row[MEDAL] != "NA":
            medal_score = {"Gold": 5, "Silver": 3, "Bronze": 1}[row[MEDAL]]
            players[row[NAME]] = players.get(row[NAME], 0) + medal_score
parser.add_argument("-top", nargs=2, help="Find top players by criteria")
parser.add_argument("-a", help="Age group (1-4)")
parser.add_argument("-w", help="Weight group (1-4)")
parser.add_argument("-height", help="Height group (1-4)")

elif args.top:
    top_n = int(args.top[0])
    gender = args.top[1]
    age_group = args.a
    weight_group = args.w
    height_group = args.height  # Заміна args.h на args.height
    top_players(file, top_n, gender, age_group, weight_group, height_group)
#     top_players = sorted(players.items(), key=lambda  x: x[1], reverse=True)[:top_n]
#
#

