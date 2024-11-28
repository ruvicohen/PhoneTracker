from flask import Blueprint, jsonify, request

phone_blueprint = Blueprint('phone_blueprint', __name__)

@phone_blueprint.route("/", methods=['POST'])
def get_interaction():
   print(request.json)
   return jsonify({ }), 200

