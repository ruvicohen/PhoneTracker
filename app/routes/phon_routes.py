from flask import Blueprint, jsonify, request

from app.service.interaction_service import process_interaction

phone_blueprint = Blueprint('phone_blueprint', __name__)

@phone_blueprint.route("/api/phone_tracker", methods=['POST'])
def get_interaction():
   interaction = request.json
   print(interaction)
   process_interaction(interaction)
   return jsonify({ }), 200

# Expose flask’s endpoint for finding all devices connected to each other using the Bluetooth method, and how long is the path.
#
# Expose flask’s endpoint for finding all devices connected to each other with a signal strength stronger than -60.
#
# Expose a Flask endpoint to count how many devices are connected to a specific device based on a provided ID.
#
# Expose a Flask endpoint to determine whether there is a direct connection between two devices.
#
# Expose a Flask endpoint to fetch the most recent interaction for a specific device, sorted by timestamp.\

@phone_blueprint.route("/api/phone_tracker/all_devices", methods=['GET'])
def get_all_devices():
   return jsonify({ }), 200

@phone_blueprint.route("/api/phone_tracker/all_devices/<id>", methods=['GET'])
def get_all_devices_by_id(id):
   return jsonify({ }), 200

@phone_blueprint.route("/api/phone_tracker/all_devices/signal_strength", methods=['GET'])
def get_all_devices_by_signal_strength():
   return jsonify({ }), 200

@phone_blueprint.route("/api/phone_tracker/all_devices/path_length", methods=['GET'])
def get_all_devices_by_path_length():
   return jsonify({ }), 200

@phone_blueprint.route("/api/phone_tracker/all_devices/direct_connection", methods=['GET'])
def get_all_devices_by_direct_connection():
   return jsonify({ }), 200

@phone_blueprint.route("/api/phone_tracker/all_devices/last_interaction", methods=['GET'])
def get_all_devices_by_last_interaction():
   return jsonify({ }), 200