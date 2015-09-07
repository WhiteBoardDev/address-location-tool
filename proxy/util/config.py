__author__ = 'cnishina'

import json
import os.path
import logging


class Config:
    def __init__(self, config_location, proxy_location):
        if not os.path.isfile(config_location):
            raise Exception("Unable to load config file")
        elif not os.path.isfile(proxy_location):
            raise Exception("Unable to load proxy config file")
        else:
            logging.info("loading configuration from " + config_location)
        self.config = json.load(file(config_location))
        self.proxy_config = json.load(file(proxy_location))
        logging.info("loaded configuration")
        logging.info(self.config)

    def get_hosts_url(self):
        return self.config["firebase"]["url"]

    def get_proxy_data(self):
        return self.proxy_config
