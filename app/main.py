from flask import Flask

from app.repository.device_repository import delete_devices
from routes.analysis_routes import phone_blueprint

app = Flask(__name__)
if __name__ == '__main__':
    delete_devices()
    app.register_blueprint(phone_blueprint, url_prefix='/api/phone_tracker')
    app.run(port=5000)