
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

elif args.top:
    top_n = int(args.top[0])
    gender = args.top[1]
    age_kategor = args.a
    weight_kategor = args.w
    height_kategor = args.height  # Заміна args.h на args.height
    top_players(file, top_n, gender, age_kategor, weight_kategor, height_kategor)

