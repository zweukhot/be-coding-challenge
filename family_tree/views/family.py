from flask import blueprints
from flask import jsonify
import family_tree.resources.family as res

blueprint = blueprints.Blueprint('family', __name__)


@blueprint.route('/health_check', methods=['GET'])
def health_check():
    return jsonify(True)


@blueprint.route('/search_person/<last_name>/<first_name>', methods=['GET'])
def search_person(last_name, first_name):
    return jsonify(res.get_person(first_name, last_name))


@blueprint.route('/get_siblings/<person_id>', methods=['GET'])
def get_siblings(person_id):
    return jsonify(res.get_siblings(person_id))


@blueprint.route('/get_parents/<person_id>', methods=['GET'])
def get_parents(person_id):
    return jsonify(res.get_parents(person_id))


@blueprint.route('/get_children/<person_id>', methods=['GET'])
def get_children(person_id):
    return jsonify(res.get_children(person_id)) 


@blueprint.route('/get_grandparents/<person_id>', methods=['GET'])
def get_grandparents(person_id):
    return jsonify(res.get_grandparents(person_id))


@blueprint.route('/get_cousins/<person_id>', methods=['GET'])
def get_cousins(person_id):
    return jsonify(res.get_cousins(person_id))




