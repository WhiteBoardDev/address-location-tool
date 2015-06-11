__author__ = 'whiteboarddev'

import sys

from util import config
from data_access import firebase_client, node_repository
import model.alt_node
from model import alt_node_factory

def alt_update():
    alt_config = config.Config(sys.argv[1])
    node_repo = node_repository.Node_Repository(firebase_client.Firebase_Client(alt_config.get_firebase_url(), alt_config.get_firebase_secret()))

    stored_node = node_repo.get_node(alt_config.get_node_name())
    actual_node = alt_node_factory.create_alt_node(alt_config.get_node_name())
    if not stored_node.equals(actual_node):
        print "Detected node differences"
        node_repo.update_node(actual_node)
    else:
        print "Skipping update, node up to date"


alt_update()
