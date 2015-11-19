__author__ = 'whiteboarddev'

import requests
import json
import socket
import netifaces
import logging

# http://stackoverflow.com/questions/270745/how-do-i-determine-all-of-my-ip-addresses-when-i-have-multiple-nics


def get_wan_ip():
    r = requests.get("https://api.ipify.org?format=json")
    json_data = json.loads(r.text)
    return json_data["ip"]


def get_lan_ip():
    for interface in netifaces.interfaces():
        try:
            for link in netifaces.ifaddresses(interface)[netifaces.AF_INET]:
                # starts with 'e' and is the last address
                if str.startswith(interface, 'e'):
                    logging.debug(link['addr'])
        except KeyError:
            pass

    return socket.gethostbyname(socket.gethostname())
