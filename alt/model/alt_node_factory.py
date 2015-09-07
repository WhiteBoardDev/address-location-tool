__author__ = 'whiteboarddev'

from util import ip_address_lookup
from model import alt_node


def create_alt_node(node_name, node_ports):
    node = alt_node.AltNode(node_name)
    node.set_ports(node_ports)
    node.set_external_address(ip_address_lookup.get_wan_ip())
    node.set_local_address(ip_address_lookup.get_lan_ip())
    return node
