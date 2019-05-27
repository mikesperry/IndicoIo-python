#!/usr/bin/python
# -*- coding: utf-8 -*-
from indicoio import personas
from .indico_text_base import TextTest

class PersonasTest(TextTest):

    def test_batch_personas(self):
        test_string = "I love my friends!"
        response = personas([test_string,test_string])
        self.assertTrue(isinstance(response, list))
        self.assertIsInstance(response[0]["commander"], float)
        self.assertEqual(response[0]["commander"], response[1]["commander"])

    def test_personas(self):
        test_string = "I love my friends!"
        response = personas(test_string)

        self.assertTrue(isinstance(response, dict))
        self.assertIsInstance(response["commander"], float)
