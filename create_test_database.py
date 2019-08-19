from family_tree.models.family import Person, ParentChild
from sqlalchemy import create_engine
try:
    from family_tree import config
except ModuleNotFoundError:
    print("ERROR: Please create a family_tree/config.py file with the USER and PASSWORD to use for database")
    exit()
user = config.USER
password = config.PASSWORD

conn_line = "postgres://{}:{}@localhost:5432".format(user, password)
pg = create_engine(conn_line)


with pg.connect() as conn:
    Person.__table__.create(pg)
    ParentChild.__table__.create(pg)

