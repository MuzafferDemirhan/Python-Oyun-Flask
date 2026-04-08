import os
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class CharacterDB(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    char_class = Column(String(20))
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    current_hp = Column(Integer)
    gold = Column(Integer, default=50)

load_dotenv()

# Baslat
DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")
SERVER = os.getenv("DB_SERVER", r"localhost\SQLEXPRESS")
DATABASE = os.getenv("DB_NAME", "RealmOfShadows")
TRUSTED = os.getenv("DB_TRUSTED_CONNECTION", "yes")
USER = os.getenv("DB_USER", "")
PASSWORD = os.getenv("DB_PASSWORD", "")

if TRUSTED.strip().lower() in {"1", "true", "yes"}:
    auth_part = "Trusted_Connection=yes;"
else:
    auth_part = f"UID={USER};PWD={PASSWORD};"

odbc_params = quote_plus(
    f"DRIVER={{{DRIVER}}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"{auth_part}"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={odbc_params}")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)