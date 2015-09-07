__author__ = 'whiteboarddev'

import json
import os.path
import logging


class Config:
    def __init__(self, config_location, alt_location):
        if not os.path.isfile(config_location):
            raise Exception("Unable to load config file")
        elif not os.path.isfile(alt_location):
            raise Exception("Unable to load alt config file")
        else:
            logging.info("loading configuration from " + config_location)
        self.config = json.load(file(config_location))
        self.alt_config = json.load(file(alt_location))
        logging.info("loaded configuration")
        logging.info(self.config)

    def get_node_name(self):
        return self.alt_config["node"]["name"]

    def get_node_ports(self):
        return self.alt_config["node"]["ports"]

    def get_firebase_url(self):
        return self.config["firebase"]["url"]

    def get_firebase_secret(self):
        return self.config["firebase"]["secret"]
