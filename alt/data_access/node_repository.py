__author__ = 'whiteboarddev'


class NodeRepository:

    def __init__(self, firebase_client):
        self.firebase_client = firebase_client

    def update_node(self, node):
        self.firebase_client.save_node(node)

    def get_node(self, node_name):
        return self.firebase_client.get_node(node_name)