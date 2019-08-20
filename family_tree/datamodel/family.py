from family_tree.models.family import Person, ParentChild
from flask import current_app


def get_person(first_name, last_name):
    query = current_app.db.session.query(
                                      Person).filter(
                                              Person.last_name==last_name,
                                              Person.first_name==first_name)
    return query.all()


def get_parents(person_id):
    query = current_app.db.session.query(
                                      ParentChild).filter(
                                              ParentChild.child == person_id)
    return query.all()


def get_children(person_id):
    query = current_app.db.session.query(
                                      ParentChild).filter(
                                              ParentChild.parent == person_id)
    return query.all()




