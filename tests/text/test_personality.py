#!/usr/bin/python
# -*- coding: utf-8 -*-
from indicoio import personality
from .indico_text_base import TextTest

class PersonalityTest(TextTest):
    def test_personalities(self):
        test_string = "I love my friends!"
        response = personality(test_string)

        categories = ['extraversion', 'openness', 'agreeableness', 'conscientiousness']
        self.assertTrue(isinstance(response, dict))
        self.assertIsInstance(response['extraversion'], float)
        for category in categories:
            assert category in response.keys()

    def test_batch_personality(self):
        test_string = "I love my friends!"
        response = personality([test_string,test_string])
        categories = ['extraversion', 'openness', 'agreeableness', 'conscientiousness']
        self.assertTrue(isinstance(response, list))
        self.assertIsInstance(response[0]["extraversion"], float)
        for category in categories:
            assert category in response[0].keys()
        self.assertEqual(response[0]["extraversion"], response[1]["extraversion"])
