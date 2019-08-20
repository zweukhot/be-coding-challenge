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
    grandpas = get_grandparents(person_id)
    parents = {parent['id']:parent
                for grandpa in grandpas 
                for parent in get_children(grandpa['id'])}
    grandchildren = {grandchild['id']:grandchild
                     for parent in parents.values()
                     for grandchild in get_children(parent['id'])}
    cousins = [grandchild for grandchild in grandchildren.values()
               if grandchild not in get_siblings(person_id)]
    return cousins


def get_grandparents(person_id):
    parents = fam_dm.get_parents(person_id)
    #we enforce uniqueness
    grandpas = {grandpa.id: grandpa
                for parent in parents
                for grandpa in fam_dm.get_parents(parent.id)}
    return person_to_list(grandpas.values())


def get_siblings(person_id):
    parents = fam_dm.get_parents(person_id)
    # enforce uniqueness
    children = {child.id: child
                for parent in parents
                for child in fam_dm.get_children(parent.id)}
    return person_to_list(children.values())


def get_children(person_id):
    query_results = fam_dm.get_children(person_id)
    return person_to_list(query_results)
