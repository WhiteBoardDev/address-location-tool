import os
import logging
import logging.config as logging_config
import sys

__author__ = 'cnishina'

linux = {
    'base_dir': '/opt/alt',
    'conf_dir': '/etc/alt/conf',
    'log_conf': '/var/log/',
}

darwin = {}

windows = {}


class Settings:

    def __init__(self):
        self.env = 'dev'
        self.run_module = None
        self.base_dir = None
        self.conf_dir = None
        self.log_conf = None

        self.db_config = None
        self.alt_config = None
        self.proxy_config = None

    # load the environment settings, default is to run as 'dev'
    def load_env(self, env):
        self.env = env

        if self.env == 'dev':
            self.base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            self.conf_dir = os.path.join(self.base_dir, 'conf')
            self.log_conf = os.path.join(self.conf_dir, 'logging.conf')
        else:
            os_setting = None
            if 'linux' in sys.platform:
                os_setting = linux
            elif 'darwin' in sys.platform:
                logging.error('mac unsupported')
                raise NotImplementedError
            elif 'win32' in sys.platform:
                logging.error('windows unsupported')
                raise NotImplementedError
            else:
                logging.error('unknown system')
                raise NotImplementedError

            self.base_dir = os_setting['base_dir']
            self.conf_dir = os_setting['conf_dir']
            self.log_conf = os_setting['log_conf']

        logging_config.fileConfig(self.log_conf)

    # load configs based on the run module
    def load_config(self, run_module):
        self.run_module = run_module
        if self.run_module == 'alt':
            self.db_config = os.path.join(self.conf_dir, 'db.json')
            self.alt_config = os.path.join(self.conf_dir, 'alt.json')
        elif self.run_module == 'proxy':
            self.db_config = os.path.join(self.conf_dir, 'db.json')
            self.proxy_config = os.path.join(self.conf_dir, 'proxy.json')
            self.alt_config = os.path.join(self.conf_dir, 'alt.json')
        elif self.run_module == 'host':
            logging.error('host unsupported')
            raise NotImplementedError
        else:
            logging.error('unknown command')
            raise RuntimeWarning
