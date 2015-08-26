__author__ = 'evanharris'

import data_access.firebase_client
import data_access.node_repository


class LifecycleManagerStaticValues:
    config = None
    firebase_client_ref = None
    node_repository_ref = None


def register_config(in_config):
    LifecycleManagerStaticValues.config = in_config

def get_config():
    return LifecycleManagerStaticValues.config

def get_firebase_client():
    if LifecycleManagerStaticValues.firebase_client_ref is None:
        LifecycleManagerStaticValues.firebase_client_ref = data_access.firebase_client.Firebase_Client(LifecycleManagerStaticValues.config.get_firebase_url(), LifecycleManagerStaticValues.config.get_firebase_secret())
    return LifecycleManagerStaticValues.firebase_client_ref

def get_node_repository():
    if LifecycleManagerStaticValues.node_repository_ref is None:
        LifecycleManagerStaticValues.node_repository_ref = data_access.node_repository.Node_Repository(get_firebase_client())
    return LifecycleManagerStaticValues.node_repository_ref

