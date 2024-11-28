from flask import Blueprint, jsonify, request

from app.service.interaction_service import process_interaction

phone_blueprint = Blueprint('phone_blueprint', __name__)

@phone_blueprint.route("/", methods=['POST'])
def get_interaction():
   interaction = request.json
   print(interaction)
   process_interaction(interaction)
   return jsonify({ }), 200

@phone_blueprint.route("/all_devices_using_bluetooth", methods=['GET'])
def get_all_devices_using_bluetooth():
   return jsonify({ }), 200

@phone_blueprint.route("/api/phone_tracker/all_devices/signal_strength", methods=['GET'])
def get_all_devices_by_signal_strength():
   return jsonify({ }), 200

@phone_blueprint.route("/api/phone_tracker/all_devices/connected_to_device", methods=['GET'])
def get_all_devices_connected_to_device():
   return jsonify({ }), 200

@phone_blueprint.route("/api/phone_tracker/direct_connection_between_two_devices", methods=['GET'])
def determine_direct_connection_between_two_devices():
   return jsonify({ }), 200

@phone_blueprint.route("/api/phone_tracker/most_recent_interaction", methods=['GET'])
def get_most_recent_interaction():
   return jsonify({ }), 200