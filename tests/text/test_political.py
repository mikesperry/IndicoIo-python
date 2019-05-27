#!/usr/bin/python
# -*- coding: utf-8 -*-


from indicoio import political
from .indico_text_base import TextTest

TEST_DATA = """
Right now, the Democratic Party, which I have called home my entire life,
is deeply in love with money. Consequently, its leaders have supported and
advanced all kinds of evil, big and small, in devotion to this love affair.
"""
POLITICAL_SET = set(['Libertarian', 'Liberal', 'Conservative', 'Green'])

class PoliticalTest(TextTest):

    def test_batch_political(self):
        response = political([TEST_DATA], version=2)
        self.assertTrue(isinstance(response, list))

    def test_political(self):
        response = political(TEST_DATA)

        self.assertTrue(isinstance(response, dict))
        self.assertEqual(POLITICAL_SET, set(response.keys()))

        test_string = "pro-choice"
        response = political(test_string, version=2)

        self.assertTrue(isinstance(response, dict))
        assert response['Libertarian'] > 0.25

    def test_political_v2(self):
        response = political(TEST_DATA, version=2)
        self.assertTrue(isinstance(response, dict))
        self.assertEqual(POLITICAL_SET, set(response.keys()))

    def test_batch_political_v2(self):
        test_data = [TEST_DATA, TEST_DATA]
        response = political(test_data, version=2)
        self.assertTrue(isinstance(response, list))
        self.assertEqual(POLITICAL_SET, set(response[0].keys()))
        self.assertEqual(response[0], response[1])
