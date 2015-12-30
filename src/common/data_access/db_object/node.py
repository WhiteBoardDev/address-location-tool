import json

__author__ = 'cnishina'


class Node:
    def __init__(self):
        self.name = None
        self.ports = None
        self.local_address = None
        self.external_address = None

    def to_json(self):
        return json.dumps(self.__dict__)

    def equals(self, other_node):
        if other_node is None:
            return False

        # split apart the ports
        ports_matches = True

        if (self.ports is not None and
                self.ports.__len__() == 0 and
                other_node.ports is None):
            ports_matches = True
        elif (self.ports is not None and
                self.ports.__len__() == 0 and
                other_node.ports == []):
            ports_matches = True
        elif (self.ports is not None and
                other_node.ports is not None and
                self.ports.__len__() == other_node.ports.__len__()):
            for self_port in self.ports:
                ports_matches &= self_port in other_node.ports
        else:
            ports_matches = False

        return (ports_matches and
                self.name == other_node.name and
                self.local_address == other_node.local_address and
                self.external_address == other_node.external_address)
