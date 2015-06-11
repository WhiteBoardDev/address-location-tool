
from util import ip_address_lookup
from model import alt_node

def create_alt_node(node_name):
    node = alt_node.ALT_NODE(node_name)
    node.set_exteral_address(ip_address_lookup.get_wan_ip())
    node.set_local_address(ip_address_lookup.get_lan_ip())
    return node
