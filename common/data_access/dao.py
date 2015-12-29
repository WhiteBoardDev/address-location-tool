import json
import logging
from common.data_access.firebase.firebase_dao import FirebaseDao

__author__ = 'cnishina'


def create(db_conf):
    json_config = json.load(file(db_conf))
    db = json_config['db']

    if db == 'firebase':
        logging.info('using firebase db')
        return FirebaseDao(db_conf)
