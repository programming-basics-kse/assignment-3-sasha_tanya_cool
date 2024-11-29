import argparse

def top_players(file, top_n, gender, age_kategor=None, weight_kategor=None):
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


