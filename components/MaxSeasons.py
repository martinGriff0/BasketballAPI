def GetMaxSeasons(seasonStats: list):
    maxPTS = [0, 0]
    maxAST = [0, 0]
    maxRB = [0, 0]
    maxSTL = [0, 0]
    maxBLK = [0,0]
    for season in seasonStats:
        if (season[27] > maxPTS[0]):
            maxPTS = season[27], season[1], "Points"
        if (season[22] > maxAST[0]):
            maxAST = season[22], season[1], "Assists"
        if (season[21] > maxRB[0]):
            maxRB = season[21], season[1], "Rebounds"
        if (season[23]):
            if (season[23] > maxSTL[0]):
                maxSTL = season[23], season[1], "Steals"
            if (season[24] > maxBLK[0]):
                maxBLK = season[24], season[1], "Blocks"
    return maxPTS, maxAST, maxRB, maxSTL, maxBLK