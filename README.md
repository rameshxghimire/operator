# portable operator service for message based apps
This service listens to MQTT events and calls required manager service based on the received message. 
This service is using the paho-mqtt library which is a third party MQTT library. 

This service needs a MQTT publisher or broadcaster running on default port 1883 and the manager service running on port 5001. 
The MQTT topic and the manager service must be registered in the config file which is not included here but can easily be inferred from the code.
