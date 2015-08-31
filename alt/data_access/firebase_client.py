__author__ = 'whiteboarddev'

import requests
import logging
import model.alt_node

from firebase_token_generator import create_token


class FirebaseClient:
    def __init__(self, firebase_url, firebase_secret):
        auth_payload = {"uid": "1"}
        self.token = create_token(firebase_secret, auth_payload)
        self.firebase_url = firebase_url

    def save_node(self, node):
        data = node.to_json()
        url = self.firebase_url + "/hosts/" + node.get_name() + ".json"
        logging.info("preparing to PUT " + url + " " + data)
        requests.put(url, data)

    def get_node(self, node_name):
        r = requests.get(self.firebase_url + "/hosts/" + node_name + ".json")
        return model.alt_node.from_json(r.text)



