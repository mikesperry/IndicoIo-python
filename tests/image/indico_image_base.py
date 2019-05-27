import os
from unittest import TestCase, SkipTest

from indicoio import config

DIR = os.path.dirname(os.path.realpath(__file__))

class ImageTest(TestCase):
    def setUp(self):
        self.api_key = config.api_key
        if not self.api_key:
            raise ValueError(
                "API Key needs to be defined in an environment variable INDICO_API_KEY to run tests."
            )

    @staticmethod
    def _require_numpy():
        try:
            import numpy as np
            return np
        except ImportError:
            raise SkipTest("Numpy is not installed!")

    def check_range(self, _list, minimum=0.9, maximum=0.1, span=0.5):
        np = self._require_numpy()
        array = np.array(_list)
        _max = np.max(array)
        _min = np.min(array)
        self.assertTrue(_max - _min > span)
