from unittest import TestCase

from indicoio import config


class PDFTestCase(TestCase):
    def setUp(self):
        self.api_key = config.api_key
        if not self.api_key:
            raise ValueError(
                "API Key needs to be defined in an environment variable INDICO_API_KEY to run tests."
            )
