import time

from generate_device_interactions.batch.phone_dispatcher import send_interactions


def run():
    while True:
        send_interactions(endpoint="http://localhost:5000/api/phone_tracker")
        time.sleep(2)

if __name__ == '__main__':
    run()