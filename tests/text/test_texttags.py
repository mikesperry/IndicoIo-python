#!/usr/bin/python
# -*- coding: utf-8 -*-


from indicoio import text_tags
from .indico_text_base import TextTest

class TextTagsTest(TextTest):

    def test_batch_texttags(self):
        test_data = ["On Monday, president Barack Obama will be..."]
        response = text_tags(test_data)
        self.assertTrue(isinstance(response, list))

    def test_text_tags(self):
        text = "On Monday, president Barack Obama will be..."
        results = text_tags(text)
        max_keys = sorted(results.keys(), key=lambda x:results.get(x), reverse=True)
        assert 'political_discussion' in max_keys[:5]
        results = text_tags(text, top_n=5)
        assert len(results) is 5
        results = text_tags(text, threshold=0.1)
        for v in results.values():
            assert v >= 0.1
