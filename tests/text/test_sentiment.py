#!/usr/bin/python
# -*- coding: utf-8 -*-
from indicoio import sentiment
from .indico_text_base import TextTest

class SentimentTest(TextTest):

    def test_sentiment(self):
        test_string = "Worst song ever."
        response = sentiment(test_string)

        self.assertTrue(isinstance(response, float))
        self.assertTrue(response < 0.5)

        test_string = "Best song ever."
        response = sentiment(test_string)
        self.assertTrue(isinstance(response, float))
        self.assertTrue(response > 0.5)

    def test_batch_sentiment(self):
        test_data = ['Worst song ever', 'Best song ever']
        response = sentiment(test_data)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(response[0] < 0.5)
