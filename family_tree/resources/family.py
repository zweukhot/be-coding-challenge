import family_tree.datamodel.family as fam_dm

def person_to_list(results):
    return [{"id": person.id,
            "first_name": person.first_name,
            "last_name": person.last_name,
            "birth_date": person.birth_date}
            for person in results]


def get_person(first_name, last_name):
    query_results = fam_dm.get_person(first_name, last_name)
    return person_to_list(query_results)


def get_parents(person_id):
    query_results = fam_dm.get_parents(person_id)
    return person_to_list(query_results)

def get_cousins(person_id):
        
    pass


def get_grandparents(person_id):
    parents = fam_dm.get_parents(person_id)
    grandpas = {grandpa.id: grandpa
                for parent in parents
                for granda in fam_dm.get_parents(parent)}
    return person_to_list(grandpas.values())


def get_siblings(person_id):
    parents = fam_dm.get_parents(person_id)
    children = {child.id: child
                for parent in parents
                for child in fam_dm.get_children(parent)}
    return person_to_list(children.values())


def get_children(person_id):
    query_results = fam_dm.get_children(person_id)
    return person_to_list(query_results)
