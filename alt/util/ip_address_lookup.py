
import requests
import json
import socket

def get_wan_ip():
    r = requests.get("https://api.ipify.org?format=json")
    json_data = json.loads(r.text)
    return json_data["ip"]

def get_lan_ip():
    return socket.gethostbyname(socket.gethostname())