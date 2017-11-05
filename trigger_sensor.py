#!/usr/bin/python

from requests import post
import time
import argparse



parser = argparse.ArgumentParser(description='Post binary state to HA')
parser.add_argument('host', metavar='Host', type=str, nargs='+',
                   help='Home Assistant hostname')
parser.add_argument('--sensor-name', default='test_sensor', type=str, dest='sensor_name', nargs=1,help='Name of binary sensor')
parser.add_argument('--friendly-name',default='Test Sensor',  type=str, dest='friendly_name', nargs=1,
                   help='Friendly name of binary sensor')
parser.add_argument('--api-password',default='thiswontwork',  type=str, dest='api_password', nargs=1,
                   help='HA API Password')

args = parser.parse_args()


host = str(args.host)[2:-2]
friendly_name = str(args.friendly_name)[2:-2]
sensor_name = str(args.sensor_name)[2:-2]
api_password = str(args.api_password)[2:-2]

url = 'http://' + host + ':8123/api/states/binary_sensor.' + sensor_name


headers = {'x-ha-access': api_password,
           'content-type': 'application/json'}

data_on = '{"state": "on", "attributes": {"friendly_name": "'+friendly_name+'"}}'
data_off = '{"state": "off", "attributes": {"friendly_name": "'+friendly_name+'"}}'

response = post(url, data=data_on, headers=headers)

print(response.text)

time.sleep(1)

response = post(url, data=data_off, headers=headers)

print(response.text)
