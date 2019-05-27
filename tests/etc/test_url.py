import unittest

from indicoio import config, fer

class TestBatchSize(unittest.TestCase):
    def setUp(self):
        self.api_key = config.api_key

        if not self.api_key:
            raise unittest.SkipTest

    def test_url_support(self):
        test_url = "https://s3-us-west-2.amazonaws.com/indico-test-data/face.jpg"
        response = fer(test_url)
        self.assertTrue(isinstance(response, dict))
        self.assertEqual(len(response.keys()), 6)
