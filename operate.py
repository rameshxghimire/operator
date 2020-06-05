#!/usr/bin/env python3

# imports
import paho.mqtt.client as mqtt
import requests
from config import Config  # all environmental variables defined in config file.


# Get the topic
TOPIC = Config.MQTT_CONFIG["topic"]

# Get the Manager service URL
BASE_URL = Config.MANAGER["url_endpoint"]


# reconnect if connection lost and then renew the subscription
# & display connection information prompt
def on_connect(client, userdata, flags, connect_status_code):
    """
    Functionality provided by the paho.mqtt library
    :param client: mqtt.Client() obj
    :param userdata:
    :param flags:
    :param connect_status_code:
    :return:
    """
    if connect_status_code == 0:
        print("Connected Successfully with MQTT Broker")
    else:
        print("Unable to Connect with MQTT Broker")

    client.subscribe(TOPIC)


# when a PUBLISH message is received from the server:
def on_message(client, userdata, msg):
    """
    print the topic, and call the manager
    :return: None
    """
    if msg.topic:
        print("Message broker says: {}".format(msg.topic))

    # call the dispatcher
    try:
        response = call_manager()
        print("\ncalling the manager service......")
        print(response)

    except Exception as e:
        print(e)


def call_manager():
    """
    make an api call to the manager service of the framework / app
    :return: str
    """
    # Provide URL endpoint of manager service
    base_url = BASE_URL
    if base_url:
        response = requests.get(base_url)
        return 200 if response.ok else 'not successful'
    else:
        return "Missing or invalid: URL endpoint of manager service"


if __name__ == "__main__":

    # Create a MQTT Client
    client = mqtt.Client()

    # Attach on_connect function to client
    client.on_connect = on_connect

    # Attach on_message function to client
    client.on_message = on_message

    # Connect with MQTT Broker on port 1883,
    client.connect(host="127.0.0.1", port=1883, keepalive=60)

    # run client in blocking mode
    client.loop_forever(timeout=1, retry_first_connection=True)
