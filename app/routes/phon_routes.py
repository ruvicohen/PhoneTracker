from flask import Blueprint, jsonify, request
from app.repository.analysis_repository import find_bluetooth_connections, devices_by_signal_strength, \
   count_connected_devices, get_most_recent_interaction_repo, determine_direct_connection_between_two_devices
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
   res = find_bluetooth_connections()
   return jsonify(res)



@phone_blueprint.route("/all_devices/signal_strength", methods=['GET'])
def get_all_devices_by_signal_strength():
   res = devices_by_signal_strength()
   return jsonify({"res": res }), 200

@phone_blueprint.route("/all_devices/connected_to_device", methods=['GET'])
def get_all_devices_connected_to_device():
   device_id = request.args.get('device_id')
   if not device_id:
      return jsonify({"error": "device_id parameter is required"}), 400
   try:
      connected_count = count_connected_devices(device_id)
      return jsonify({"device_id": device_id, "connected_count": connected_count}), 200
   except Exception as e:
      return jsonify({"error": str(e)}), 500


@phone_blueprint.route("/direct_connection_between_two_devices", methods=['GET'])
def determine_direct_connection_between_two_devices_route():
   device_id_1 = request.args.get('device_id_1')
   device_id_2 = request.args.get('device_id_2')

   if not device_id_1 or not device_id_2:
      return jsonify({"error": "Both device_id_1 and device_id_2 parameters are required"}), 400

   try:
      # Check if the devices are directly connected
      is_connected = determine_direct_connection_between_two_devices(device_id_1, device_id_2)
      return jsonify({
         "device_id_1": device_id_1,
         "device_id_2": device_id_2,
         "connected": is_connected
      }), 200

   except Exception as e:
      return jsonify({"error": str(e)}), 500


@phone_blueprint.route("/most_recent_interaction", methods=['GET'])
def get_most_recent_interaction():
   device_id = request.args.get('device_id')
   if not device_id:
      return jsonify({"error": "device_id parameter is required"}), 400
   try:
      timestamp = get_most_recent_interaction_repo(device_id)
      return jsonify({"device_id": device_id, "timestamp": timestamp}), 200
   except Exception as e:
      return jsonify({"error": str(e)}), 500