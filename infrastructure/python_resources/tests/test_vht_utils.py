import unittest
import os

from vht.vht_utils import VhtUtils

class TestVhtUtils(unittest.TestCase):
    def test_is_aws_credentials_present(self):
        utils = VhtUtils()
        utils.is_aws_credentials_present()

if __name__ == '__main__':
    unittest.main()
