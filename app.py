import sys

from alt.alt import Alt
from proxy.proxy import Proxy
from common.settings import Settings

__author__ = 'cnishina'


def main():
    env = sys.argv[1]
    run = sys.argv[2]
    settings = Settings()
    settings.load_env(env)

    if run == 'alt':
        settings.load_config(run)
        alt = Alt(settings.alt_config, settings.db_config)
        alt.update()
    elif run == 'proxy':
        settings.load_config(run)
        proxy = Proxy(settings.alt_config, settings.proxy_config, settings.db_config)
        proxy.update()
    # elif run == 'host':
    #     logging.info('proxy')
    # else:
    #     logging.error('unknown command')


main()
