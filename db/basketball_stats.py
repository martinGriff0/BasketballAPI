from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://admin:SageJutsu69@basketball-search.cq86yhnzjvtt.us-east-1.rds.amazonaws.com/sys", echo=True, future=True)