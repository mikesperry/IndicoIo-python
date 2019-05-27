#!/usr/bin/python
# -*- coding: utf-8 -*-


from indicoio import relevance
from .indico_text_base import TextTest
import numpy as np

class RelevanceTest(TextTest):

    def test_relevance(self):
        test_data = 'president'
        test_query = ['president', "prime minister"]
        response = relevance(test_data, test_query)
        self.assertTrue(isinstance(response, np.ndarray))
        self.assertTrue(response[0] > 0.5)
        self.assertTrue(response[1] > 0.2)
        self.assertEqual(len(response), 2)

    def test_batch_relevance(self):
        test_data = ['president', 'president']
        test_query = ['president', "prime minister"]
        response = relevance(test_data, test_query)
        self.assertTrue(isinstance(response, np.ndarray))
        self.assertTrue(response[0][0] > 0.5)
        self.assertTrue(response[0][1] > 0.2)
        self.assertEqual(len(response), 2)
        self.assertEqual(len(response[0]), 2)
        self.assertEqual(len(response[1]), 2)
