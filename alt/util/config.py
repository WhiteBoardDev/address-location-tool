__author__ = 'whiteboarddev'

import json
import os.path
import logging


class Config:
    def __init__(self, config_location):
        if not os.path.isfile(config_location):
            raise Exception("Unable to load config file")
        else:
            logging.info("loading configuration from " + config_location)
        self.config = json.load(file(config_location))
        logging.info("loaded configuration")
        logging.info(self.config)

    def get_node_name(self):
        return self.config["node"]["name"]

    def get_firebase_url(self):
        return self.config["firebase"]["url"]

    def get_firebase_secret(self):
        return self.config["firebase"]["secret"]
