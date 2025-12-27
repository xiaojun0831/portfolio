import random


def get_rand_word():
    words = ["HAPPY", "TRAIN", "SMILE", "CRANE", "PLANE", "CROWN", "QUEEN",
             "LASER", "FLOUR", "CHORD", "SNAIL", "SPACE", "RADIO", "GRACE",
             "WHALE", "HORSE", "TIGER", "TRUCK", "CRAVE", "BRIDE", "GROOM",
             "STUMP", "SLANT", "POWER", "LABEL", "FRESH", "SLIDE", "HOUSE",
             "HOME", "TIRE", "BEAR", "CORE", "CURE", "ABLE", "SHOT",
             "TREE", "BAIL", "PAIL", "MAIL", "FREE", "FIRE", "FALL",
             "BALL", "POND", "PARK", "WINE", "DARE", "DONE", "PUCK",
             "HARE", "HAIR", "BILL", "FISH", "PILE", "WAIT", "NAIL"
             ]
    return random.choice(words)
