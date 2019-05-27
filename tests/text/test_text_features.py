#!/usr/bin/python
# -*- coding: utf-8 -*-


from indicoio import text_features
from .indico_text_base import TextTest
import numpy as np

class TextFeaturesTest(TextTest):

    def test_text_features(self):
        test_data = 'Queen of England'
        response = text_features(test_data)
        self.assertTrue(isinstance(response, np.ndarray))
        self.assertEqual(len(response), 300)

    def test_batch_text_features(self):
        test_data = ['Queen of England', 'Prime Minister of Canada']
        response = text_features(test_data)
        self.assertTrue(isinstance(response, np.ndarray))
        self.assertEqual(len(response), 2)
        self.assertEqual(len(response[0]), 300)
        self.assertEqual(len(response[1]), 300)
