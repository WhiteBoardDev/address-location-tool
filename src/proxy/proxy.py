from common.config.alt_config import AltConfig
from common.config.proxy_config import ProxyConfig
import common.data_access.dao as dao
import nginx

__author__ = 'cnishina'


class Proxy:
    def __init__(self, alt_conf, proxy_conf, db_conf):
        self.alt_config = AltConfig(alt_conf)
        self.proxy_config = ProxyConfig(proxy_conf)
        self.dao = dao.create(db_conf)

    def update(self):
        # pull down hosts.json and parse to a model
        all_nodes = self.dao.get_all_nodes()
        nginx.build_proxy_file(all_nodes, self.proxy_config)

