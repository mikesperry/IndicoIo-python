import unittest
from requests import ConnectionError

from indicoio import config, language, IndicoError

class SetConfigsTest(unittest.TestCase):
    def setUp(self):
        self.api_key = config.api_key

        if not self.api_key:
            raise unittest.SkipTest

    def test_set_api_key(self):
        test_data = 'clearly an english sentence'
        self.assertRaises(IndicoError,
                          language,
                          test_data,
                          api_key ='invalid_api_key')

        temp_api_key = config.api_key
        config.api_key = 'invalid_api_key'

        self.assertEqual(config.api_key, 'invalid_api_key')
        self.assertRaises(IndicoError,
                          language,
                          test_data)

        config.api_key = temp_api_key


    def test_set_cloud(self):
        test_data = 'clearly an english sentence'
        self.assertRaises(ConnectionError,
        language,
        test_data,
        cloud='invalid/cloud')

        temp_cloud = config.cloud
        config.cloud = 'invalid/cloud'

        self.assertEqual(config.cloud, 'invalid/cloud')
        self.assertRaises(ConnectionError,
        language,
        test_data)

        config.cloud = temp_cloud

    def test_batch_set_cloud(self):
        test_data = ['clearly an english sentence']
        self.assertRaises(ConnectionError,
                          language,
                          test_data,
                          api_key=self.api_key,
                          cloud='invalid/cloud')
