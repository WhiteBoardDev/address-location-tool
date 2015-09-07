__author__ = 'cnishina'


class LifecycleManagerStaticValues:
    config = None

    def __init__(self):
        return


def register_config(in_config):
    LifecycleManagerStaticValues.config = in_config


def get_config():
    return LifecycleManagerStaticValues.config
