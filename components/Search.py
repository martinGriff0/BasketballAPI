from ast import operator
from os import times
import random
from turtle import position
from components.Models import Item 
from components.Arrays import IntSubItems, Operators
from db.basketball_stats import engine
from sqlalchemy import text
from components.Value import GetValue
from components.MaxSeasons import GetMaxSeasons

def CustomSearch(item: Item):
    searchString = "select * from per_game_seasons where "
    count = 0
    for ite in item:
        if ite[1].value and ite[1].value.strip():
            if count > 0:
                searchString = searchString + " AND "
            if ite[1].string in IntSubItems:
                searchString = searchString + ite[1].string + " " + ite[1].operator + " " + ite[1].value
            else:
                searchString = searchString + ite[1].string + " like '%" + ite[1].value + "%'"
            count = count + 1
    return searchString + " ORDER BY Year Desc"

def RandomSearch(num: int):
    tIntsubItems = list(IntSubItems)
    tIntsubItems.remove("Year")
    count = num + 1
    searchString = "select * from per_game_seasons where "
    times = 0
    operator = ">"
    with engine.connect() as conn:
        while count > num or count == 0 :
            if count == 0 or times >= len(IntSubItems):
                searchString = "select * from per_game_seasons where "
                tIntsubItems = list(IntSubItems)
                tIntsubItems.remove("Year")
                times = 0
            intSubItem = random.choice(tIntsubItems)
            tIntsubItems.remove(intSubItem)
            value, operator = GetValue(intSubItem)
            # operator = random.choice(Operators)


            if times == 0:
                searchString = searchString + intSubItem + " " + operator + " " + str(value)
            else:
                searchString = searchString + " AND " + intSubItem + " " + operator + " " + str(value)
            result = conn.execute(text(searchString))
            response = result.all()
            count = len(response)
            times = times + 1

        finalSearchString = searchString.removeprefix("select * from per_game_seasons where ")
        return response, finalSearchString

    
def GetPlayerPage(playerName: str):
    with engine.connect() as conn:
        result = conn.execute(text('select * from per_game_seasons where name = "{0}" ORDER By Year'.format(playerName)))
        seasonStats = result.all()
        positions = []
        teams = []
    for season in seasonStats:
        if (season[3] not in positions):
            if '-' in season[3]:
                twoPos = season[3].split('-')
                for pos in twoPos:
                    positions.append(pos)
            else:
                positions.append(season[3])
            positions = list(dict.fromkeys(positions))
        if (season[5] not in teams):
            if season[5] != "TOT":
                teams.append(season[5])
    bestSeasons = GetMaxSeasons(seasonStats)
    return seasonStats, teams, positions, bestSeasons
