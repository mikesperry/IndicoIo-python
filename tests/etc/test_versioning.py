#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, unittest

from indicoio import sentiment
from indicoio import image_features
from indicoio import config

DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "image")
class TestVersioning(unittest.TestCase):
    def setUp(self):
        self.api_key = config.api_key

    def test_specify_version(self):
        test_data = ['Worst song ever', 'Best song ever']
        response = sentiment(test_data, version="1")
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 2)
        self.assertTrue(response[0] < .5)
        self.assertTrue(response[1] > .5)

    def test_image_features_v2(self):
        test_data = os.path.normpath(os.path.join(DIR, "data", "fear.png"))
        response = image_features(test_data, version="2")
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 4096)

if __name__ == "__main__":
    unittest.main()
