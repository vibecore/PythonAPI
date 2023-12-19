from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
import pymssql
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = 'mssql+pymssql://{0}:{1}@{2}\\{3}/{5}?charset=utf8'.format(
            settings.database_username,
            quote_plus(settings.database_password),
            settings.database_hostname,
            settings.database_instance,
            settings.database_port,
            settings.database_name
        )

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

# while True:
#     try:
#         conn = pymssql.connect(
#             server="localhost\\SQL2019",
#             user="PythonAPI",
#             password="@l3X3mm@97!",
#             database="PythonAPI",
#             as_dict=True
#         )

#         cursor = conn.cursor(as_dict=True)
#         print("Database Connection was successful!") 
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()