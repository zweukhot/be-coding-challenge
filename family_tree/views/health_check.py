from flask import blueprints
from flask import jsonify
import family_tree.resources.family as res

blueprint = blueprints.Blueprint('health_check', __name__)


@blueprint.route('/health_check', methods=['GET'])
def health_check():
    return jsonify(True)


@blueprint.route('/<person_id>/get_siblings', methods=['GET'])
def get_siblings(person_id):
    return jsonify(res.get_siblings(person_id))


@blueprint.route('/<person_id>/get_parents', methods=['GET'])
def get_parents(person_id):
    return jsonify(res.get_parents(person_id))

@blueprint.route('/<person_id>/get_children', methods=['GET'])
def get_children(person_id):
    return jsonify(res.get_children(person_id)) 


@blueprint.route('/<person_id>/get_grandparents', methods=['GET'])
def get_grandparents(person_id):
    return jsonify(res.get_grandparents(person_id))


@blueprint.route('/<person_id>/get_cousins', methods=['GET'])
def get_cousins(person_id):
    return jsonify(res.get_cousins(person_id))




