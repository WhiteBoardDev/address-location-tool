import json
import logging
import requests
import common.data_access.firebase.token_generator as token_generator
from common.data_access.db_object.node import Node

__author__ = 'cnishina'


class FirebaseConfig:
    def __init__(self, db_conf):
        json_config = json.load(file(db_conf))
        self.db = json_config['db']
        self.url = json_config['config']['url']
        self.secret = json_config['config']['secret']


class FirebaseDao:
    def __init__(self, db_conf):
        firebase_config = FirebaseConfig(db_conf)
        firebase_url = firebase_config.url
        firebase_secret = firebase_config.secret

        auth_payload = {"uid": "1"}
        self.token = token_generator.create_token(firebase_secret, auth_payload)
        self.firebase_url = firebase_url

    def save_node(self, node):
        data = node.to_json()
        url = self.firebase_url + "/hosts/" + node.name + ".json"
        logging.debug("preparing to PUT " + url)
        logging.debug(data)
        requests.put(url, data)

    def get_node(self, node_name):
        r = requests.get(self.firebase_url + "/hosts/" + node_name + ".json")
        json_data = json.loads(r.text)
        if json_data is not None:
            node = Node()
            node.name = json_data['name']
            if 'ports' in json_data:
                node.ports = json_data['ports']
            node.local_addresses = json_data['local_addresses']
            node.external_address = json_data['external_address']
            node.changed_time = json_data['changed_time']
            node.changed_time_human = json_data['changed_time_human']
            return node
        else:
            return None

    def get_all_nodes(self):
        r = requests.get(self.firebase_url + "/hosts.json")
        nodes = []
        json_data = json.loads(r.text)
        if json_data is not None:
            for key in json_data.keys():
                node = Node()
                node.name = key
                if 'ports' in json_data[key]:
                    node.ports = json_data[key]['ports']
                node.local_addresses = json_data[key]['local_addresses']
                node.external_address = json_data[key]['external_address']
                node.changed_time = json_data[key]['changed_time']
                node.changed_time_human = json_data[key]['changed_time_human']
                nodes.append(node)
        return nodes




