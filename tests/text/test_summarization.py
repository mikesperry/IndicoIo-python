import os

from indicoio import summarization
from .indico_text_base import TextTest, DIR

with open(os.path.join(DIR, "data", "long_text.txt"), 'rb') as fd:
    TEXT_DATA = fd.read()

class SummarizationTest(TextTest):

    def test_summarization(self):
        response = summarization(TEXT_DATA, top_n=5)
        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 5)

