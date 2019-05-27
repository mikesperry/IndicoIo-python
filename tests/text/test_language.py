#!/usr/bin/python
# -*- coding: utf-8 -*-

from indicoio import language
from .indico_text_base import TextTest

LANGUAGES = set([
    'English', 'Spanish', 'Tagalog', 'Esperanto', 'French',
    'Chinese', 'French', 'Bulgarian', 'Latin', 'Slovak',
    'Hebrew', 'Russian', 'German', 'Japanese', 'Korean',
    'Portuguese', 'Italian', 'Polish', 'Turkish', 'Dutch',
    'Arabic', 'Persian (Farsi)', 'Czech', 'Swedish', 'Indonesian',
    'Vietnamese', 'Romanian', 'Greek', 'Danish', 'Hungarian',
    'Thai', 'Finnish', 'Norwegian', 'Lithuanian'
])

class LanguageTest(TextTest):

    def test_language(self):
        language_dict = language('clearly an english sentence')
        self.assertEqual(LANGUAGES, set(language_dict.keys()))
        assert language_dict['English'] > 0.25

    def test_batch_language(self):
        test_data = ['clearly an english sentence']
        response = language(test_data)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(response[0]['English'] > 0.25)
