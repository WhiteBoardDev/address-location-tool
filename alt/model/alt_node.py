import json

class ALT_NODE:
    def __init__(self, name):
        self.name = name

    def set_exteral_address(self,external_address):
        self.external_address = external_address

    def set_local_address(self, local_address):
        self.local_address = local_address

    def get_name(self):
        return self.name

    def get_local_address(self):
        return self.local_address

    def get_external_address(self):
        return self.external_address

    def to_json(self):
        return json.dumps(self.__dict__)

    def equals(self, other_alt_node):
        return (self.get_name() == other_alt_node.get_name() and
                self.get_local_address() == other_alt_node.get_local_address() and
                self.get_external_address() == other_alt_node.get_external_address())



def from_json(json_text):
    json_data = json.loads(json_text)
    node = ALT_NODE(json_data['name'])
    node.set_local_address(json_data['local_address'])
    node.set_exteral_address(json_data['external_address'])
    return node
