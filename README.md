# trigger-sensor
Python script to trigger a binary sensor in Home Assistant via the API

usage: trigger_sensor.py [-h] [--sensor-name SENSOR_NAME]
                         [--friendly-name FRIENDLY_NAME]
                         [--api-password API_PASSWORD]
                         Host [Host ...]

positional arguments:
  Host                  Home Assistant hostname

optional arguments:

  -h, --help            show this help message and exit

  --sensor-name SENSOR_NAME - This is the internal name of the binary sensor to be created

  --friendly-name FRIENDLY_NAME - This is the friendly / display name of the sensor

  --api-password API_PASSWORD - This is your API password

You can use this script within the Xeoma video surveillance software (http://felenasoft.com/xeoma/en/) to integrate motion events into Home Assistant (https://home-assistant.io/).

Use the Application Runner component, connected after the motion sensor component to call this script. The script will automatically create a Binary Sensor within Home Assistant based on the sensor name you provide. The script fires an "On" followed 1 second later by an "Off" event. 


