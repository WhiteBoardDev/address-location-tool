import logging
import sys

from alt.alt import Alt
from host.host import Host
from proxy.proxy import Proxy
from common.settings import Settings

__author__ = 'cnishina'


def main():
    run = sys.argv[1]
    env = None
    if sys.argv.__len__() == 3:
        env = sys.argv[2]

    try:
        settings = Settings()
        settings.load_env(env)
        settings.load_config(run)
        if run == 'alt':
            alt = Alt(settings.alt_config, settings.db_config)
            alt.update()
        elif run == 'proxy':
            proxy = Proxy(settings.alt_config, settings.proxy_config, settings.db_config)
            proxy.update()
        elif run == 'hosts':
            host = Host(settings.db_config, settings.hosts_read, settings.hosts_write)
            host.update()
        else:
            logging.error('unknown run module')
            raise RuntimeError
    except RuntimeWarning:
        pass
    except NotImplementedError:
        pass


main()
