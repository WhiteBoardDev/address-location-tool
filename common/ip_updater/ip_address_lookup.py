import requests
import json
import socket
import netifaces
import logging

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
            for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                # starts with 'e' and is the last address
                if str.startswith(interface, 'e'):
                    logging.debug('internal address: ' + link['addr'])
        except KeyError:
            pass

    return unicode(socket.gethostbyname(socket.gethostname()))
