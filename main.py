import os
import imp
from multiprocessing.sharedctypes import Value
from unicodedata import name
from urllib import response
from fastapi import FastAPI
from sqlalchemy.sql.expression import and_
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from components.Search import CustomSearch, GetPlayerPage, RandomSearch
from components.Models import Item
from db.basketball_stats import engine
from mangum import Mangum

# stage = os.environ.get('STAGE', None)
# openapi_prefix = f"/{stage}" if stage else "/"
app = FastAPI(title="BasketballDatabase")

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000/",
    "http://127.0.0.1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# engine = create_engine("mysql+pymysql://root:ilikemen69@127.0.0.1/Basketball", echo=True, future=True)

@app.get("/")
async def root():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT Year, Name Year FROM per_game_seasons WHERE RB > 20"))
    response = result.all()
    return response

@app.post("/")
async def ccustom_search(item: Item):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(CustomSearch(item)))
        response = result.all()
        return response
    except:
        return "Error", "There was an Error"

    
@app.post("/RandomSearch")
async def random_search(count: int):
    try:
        response = RandomSearch(count)
        return response
    except:
        return "Error", "There was an Error, please try again"

@app.get("/Player")
async def get_player_page(playerName: str):
    try:
        response = GetPlayerPage(playerName)
        return response
    except:
        return "There was an Error"

@app.post("/RandomSearch/Quiz")
async def quiz_question():
    try:
        randomSearch = RandomSearch(6)
        nameArray = []
        for season in randomSearch[0]:
            if "*" in season[2]:
                name = season[2].replace("*", "")
                if name not in nameArray:
                    nameArray.append(name)
            else:
                if season[2] not in nameArray:
                    nameArray.append(season[2])
        amount = len(randomSearch[0]), len(nameArray)
        hint = randomSearch[0][0][1], randomSearch[0][0][5], randomSearch[0][0][3]
        return randomSearch[1], nameArray, amount, hint
    except:
        return "Error", "There was an Error, please try again"

@app.get("/Leaderboard/Top")
async def current_leader():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT leaderboardId AS id, Name, Score FROM leaderboard ORDER BY Score DESC"))
        response = result.all()
        return response
    except:
        return "Error", "There was an Error, please try again"

@app.post("/Leaderboard/Add")
async def add_score(name: str, score: int):
    try:
        with engine.connect() as conn:
            finalName = name.strip()
            conn.execute(text('INSERT INTO leaderboard (Name, Score) VALUES ("{0}", {1})'.format(finalName, score)))
            conn.commit()
        return "Success"
    except:
        return "Error", "There was an Error, please try again"

handler = Mangum(app)