from family_tree.models.family import Person, ParentChild
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

Session = sessionmaker(bind=pg)
session = Session()
fams = [Person(first_name="grandpa", last_name="smith"),
        Person(first_name="grandma", last_name="smith"),
        Person(first_name="papa", last_name="smith"),
        Person(first_name="mama", last_name="smith"),
        Person(first_name="lil_timmy", last_name="smith"),
        Person(first_name="lil_jane", last_name="smith"),
        Person(first_name="aunty", last_name="smith"),
        Person(first_name="uncle_joe", last_name="smith"),
        Person(first_name="cousin_vinny", last_name="smith")]
session.add_all(fams)
session.commit()
relations = [ ParentChild(parent_id=1, child_id=3),
              ParentChild(parent_id=2, child_id=3),
              ParentChild(parent_id=3, child_id=5),
              ParentChild(parent_id=4, child_id=5),
              ParentChild(parent_id=3, child_id=6),
              ParentChild(parent_id=4, child_id=6),
              ParentChild(parent_id=1, child_id=7),
              ParentChild(parent_id=2, child_id=7),
              ParentChild(parent_id=7, child_id=9),
              ParentChild(parent_id=8, child_id=9)]
session.add_all(relations)
session.commit()
