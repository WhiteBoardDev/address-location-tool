__author__ = 'whiteboarddev'

import sys
from util import config
from model import alt_node_factory
import logging
import logging.config
from util import lifecycle_manager


def alt_update():

    logging.config.fileConfig('logging.conf')

    # bootstrap application by setting configs
    lifecycle_manager.register_config(config.Config(sys.argv[1]))

    config_data = lifecycle_manager.get_config()
    node_repo = lifecycle_manager.get_node_repository()

    stored_node = node_repo.get_node(config_data.get_node_name())
    actual_node = alt_node_factory.create_alt_node(config_data.get_node_name())
    if stored_node is None or not stored_node.equals(actual_node):
        logging.info("Detected node differences")
        node_repo.update_node(actual_node)
    else:
        logging.info("Skipping update, node up to date")


alt_update()
