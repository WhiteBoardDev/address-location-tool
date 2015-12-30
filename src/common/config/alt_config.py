import json

__author__ = 'cnishina'


class AltConfig:

    def __init__(self, alt_config):
        json_config = json.load(file(alt_config))
        self.node_name = json_config['node']['name']
        self.node_ports = json_config['node']['ports']
