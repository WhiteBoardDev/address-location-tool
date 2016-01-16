__author__ = 'evanharris'

import ip_address_lookup
import unittest


class GetLanIpWhenLoopBackIsFirst(unittest.TestCase):
    def runTest(self):
        lan = ip_address_lookup.get_lan_ip()
        assert lan.__sizeof__() > 0
