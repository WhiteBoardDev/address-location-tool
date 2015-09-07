__author__ = 'cnishina'

import sys
from util import nginx
from util.config import Config
import logging
import logging.config
from util import lifecycle_manager


def alt_proxy():
    logging.config.fileConfig('logging.conf')

    # read in config
    lifecycle_manager.register_config(Config(sys.argv[1], sys.argv[2]))
    config = lifecycle_manager.get_config()

    # pull down hosts.json and parse to a model
    hosts_data = nginx.get_hosts(config.get_hosts_url() + '/hosts.json')
    proxy_data = config.get_proxy_data()

    nginx.build_proxy_file(hosts_data, proxy_data)

    # write nginx file


alt_proxy()



