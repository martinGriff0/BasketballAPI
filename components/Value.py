import random
from components.Arrays import Operators

def GetValue(category: str):
    if category == "PTS":
        return random.randrange(5, 39), ">"
        # return round((random.random() * 35) + 5, 1)
    elif category == "AGE":
        return random.randrange(20, 36), random.choice(Operators)
    elif category == "AST" or category == "RB":
        return random.randrange(3, 18), ">"
        # return round((random.random() * 15) + 3, 1)
    elif category == "BLK" or category == "STL":
        return random.randrange(1, 5), ">"
        # return round((random.random() * 5) + .5, 1)
    elif category == "TOV":
        return random.randrange(1, 5), "<"
    elif category == "Year":
        return random.randrange(1959, 2020), random.choice(Operators)
    # elif category == "FG" or category == "FGA":
    #     return random.randrange(5, 20), ">"
    # elif category == "3P" or category == "3PA":
    #     return random.randrange(2, 10), ">"
    # elif category == "FGPer" or category == "3PPer":
    #     return (random.random() * .35) + .3, ">"
