from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#DATABASE_URL = "mysql+pymysql://root:Newsuer@123@localhost:3306/Property_Details"
#DATABASE_URL = "mysql+pymysql://root:Newuser%40123@localhost:3306/Property_Details"
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_gUuOkRmdOYTlF1zLGZF@mysql-2de7fbee-bharatbsingh81-4673.j.aivencloud.com:11584/Property_Details"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()