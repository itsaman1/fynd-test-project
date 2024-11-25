from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

DATABASE_URL = "sqlite:///database.db"

engine = create_engine("mysql+pymysql://itsaman22:Roorkee2207@itsaman22.mysql.pythonanywhere-services.com:3306/fynd")
Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
# class return karega phir iska object bnanan padega
session = Session()



