import family_tree.datamodel.family
from flask import current_app
from family_tree.models.family import Person, ParentChild

def get_person(first_name, last_name):
    query = current_app.db.session.query(Person).filter(Person.last_name==last_name,
                                     Person.first_name==first_name)
    return query.all()


def get_parents(person_id):
    pass


def get_cousins(person_id):
    pass


def get_grandparents(person_id):
    pass


def get_siblings(person_id):
    pass


def get_children(person_id):
    pass
