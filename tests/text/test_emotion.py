#!/usr/bin/python
# -*- coding: utf-8 -*-

from indicoio import emotion
from .indico_text_base import TextTest

class EmotionTest(TextTest):

    def test_emotion(self):
        data = "I did it. I got into Grad School. Not just any program, but a GREAT program. :-)"
        response = emotion(data)

        self.assertTrue(isinstance(response, dict))
        self.assertIsInstance(response["joy"], float)

    def test_batch_emotion(self):
        test_data = ["I did it. I got into Grad School. Not just any program, but a GREAT program. :-)"]
        response = emotion(test_data)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(isinstance(response[0], dict))
        self.assertIn('joy', response[0].keys())
