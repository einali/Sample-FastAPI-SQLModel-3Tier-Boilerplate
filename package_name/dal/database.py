from package_name.utils.setting import project_setting
from sqlalchemy import URL
from sqlalchemy.exc import SQLAlchemyError


from sqlmodel import Field, Session, SQLModel, create_engine, select

dbURL = URL.create(
    drivername=project_setting.PG_DRIVERNAME,
    username=project_setting.PG_USER,
    password=project_setting.PG_PASSWORD,
    database=project_setting.PG_DBNAME,
    host=project_setting.PG_HOST,
    port=project_setting.PG_PORT
)
engine = create_engine(dbURL,pool_size=40, max_overflow=0, echo=True)



def get_session():
    session = Session(engine)
    try:
        yield session
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()
