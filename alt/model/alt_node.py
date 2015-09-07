__author__ = 'whiteboarddev'

import json


class AltNode:

    def __init__(self, name):
        self.name = name
        self.ports = None
        self.external_address = None
        self.local_address = None

    def set_external_address(self, external_address):
        self.external_address = external_address

    def set_local_address(self, local_address):
        self.local_address = local_address

    def set_ports(self, ports):
        self.ports = ports

    def get_name(self):
        return self.name

    def get_local_address(self):
        return self.local_address

    def get_external_address(self):
        return self.external_address

    def to_json(self):
        return json.dumps(self.__dict__)

    def equals(self, other_alt_node):
        # split apart the ports
        ports_matches = True
        if (self.ports is not None
                and other_alt_node.ports is not None
                and self.ports.__len__() == other_alt_node.ports.__len__()):
            for self_port in self.ports:
                ports_matches &= self_port in other_alt_node.ports
        else:
            ports_matches = False

        return (ports_matches and
                self.get_name() == other_alt_node.get_name() and
                self.get_local_address() == other_alt_node.get_local_address() and
                self.get_external_address() == other_alt_node.get_external_address())


def from_json(json_text):
    json_data = json.loads(json_text)
    if json_data is not None:
        node = AltNode(json_data['name'])
        if 'ports' in json_data:
            node.set_ports(json_data['ports'])
        node.set_local_address(json_data['local_address'])
        node.set_external_address(json_data['external_address'])
        return node
    else:
        return None
