from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db_url = "postgresql+psycopg2://postgres:AcademyRootPassword@localhost:5432/click2pass_backend"

engine = create_engine(db_url)  
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
