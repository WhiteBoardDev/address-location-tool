import requests
import json
import socket
import netifaces
import logging
from array import *

__author__ = 'whiteboarddev'


def get_wan_ip():
    r = requests.get("https://api.ipify.org?format=json")
    json_data = json.loads(r.text)
    logging.debug('external address: ' + json_data["ip"])
    return json_data["ip"]


# inspired by:
# http://stackoverflow.com/questions/270745/how-do-i-determine-all-of-my-ip-addresses-when-i-have-multiple-nics

def get_lan_ip():
    for interface in netifaces.interfaces():
        try:
            internal_addresses = []
            internal_addresses.append(socket.gethostbyname(socket.gethostname()))
            for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                if str.startswith(interface, 'e'):
                    internal_address = link['addr']
                    logging.debug('internal address: ' + internal_address)
                    internal_addresses.append(internal_address)
        except KeyError:
            pass
    return internal_addresses
