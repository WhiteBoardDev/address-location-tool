import logging
import common.data_access.dao as dao
import common.ip_updater.ip_address_lookup as ip_address_lookup
from common.config.alt_config import AltConfig
from common.data_access.db_object.node import Node

__author__ = 'cnishina'


class Alt:
    def __init__(self, alt_conf, db_conf):
        self.alt_config = AltConfig(alt_conf)
        self.dao = dao.create(db_conf)

    # get the node from the db and create or update if necessary
    def update(self):
        read_node = self.dao.get_node(self.alt_config.node_name)
        update_node = Node()
        update_node.name = self.alt_config.node_name
        update_node.ports = self.alt_config.node_ports
        update_node.external_address = ip_address_lookup.get_wan_ip()
        update_node.local_address = ip_address_lookup.get_lan_ip()

        if update_node.equals(read_node):
            logging.info('skipping update for node: ' + self.alt_config.node_name)
        else:
            logging.info('updating / creating node: ' + self.alt_config.node_name)
            self.dao.save_node(update_node)

