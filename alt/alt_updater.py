__author__ = 'whiteboarddev'

import sys
from util import config
from model import alt_node_factory
import logging
from util import LifecycleManager
def alt_update():
    #bootstrap application by setting configs
    LifecycleManager.register_config(config.Config(sys.argv[1]))
    config_data = LifecycleManager.get_config()
    node_repo = LifecycleManager.get_node_repository()
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    stored_node = node_repo.get_node(config_data.get_node_name())
    actual_node = alt_node_factory.create_alt_node(config_data.get_node_name())
    if stored_node is None or not stored_node.equals(actual_node):
        logging.info("Detected node differences")
        node_repo.update_node(actual_node)
    else:
        logging.info("Skipping update, node up to date")


alt_update()
