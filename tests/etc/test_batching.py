import unittest
import glob
import os
import json

import numpy as np

from indicoio import config, sentiment_hq, IndicoError


class TestBatchSize(unittest.TestCase):
    def setUp(self):
        self.api_key = config.api_key

        if not self.api_key:
            raise unittest.SkipTest

    def test_batch_size(self):
        test_data = ["Terribly interesting test data."] * 100
        response = sentiment_hq(test_data, batch_size=20)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(all([isinstance(el, (float, np.float32)) for el in response]))

    def test_batched_error_handling(self):
        test_data = ["Terribly interesting test data."] * 100
        test_data[98] = ""
        with self.assertRaises(IndicoError):
            sentiment_hq(test_data, batch_size=20)

        files = glob.glob('indico-sentimenthq-*.json')
        assert len(files)

        for filename in files:
            data = json.load(open(filename, 'r'))

            # first four batches should have returned
            assert len(data) == 80

            # clean up after ourselves
            os.remove(filename)
