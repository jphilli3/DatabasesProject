from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:dbpw@localhost:5432/db-proj"
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:dbpw@localhost/guitar_db'

## TRIP USE THIS ONE
#yySQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:mypassword@localhost/guitar_database'

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()