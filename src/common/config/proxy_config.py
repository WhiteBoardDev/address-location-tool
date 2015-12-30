import json

__author__ = 'cnishina'


class ProxyPorts:
    def __init__(self):
        self.internal = None
        self.external = None


class ProxyConfig:
    def __init__(self, alt_config):
        json_config = json.load(file(alt_config))
        self.domain_name = json_config['domain']
        self.proxies = []

        proxies = json_config['proxies']
        for proxy in proxies:
            proxy_ports = ProxyPorts()
            proxy_ports.internal = proxy['internal']
            proxy_ports.external = proxy['external']
            self.proxies.append(proxy_ports)

