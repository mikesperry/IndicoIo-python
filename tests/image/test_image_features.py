#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from indicoio import image_features, IndicoError
from .indico_image_base import ImageTest, DIR

class ImageFeaturesTest(ImageTest):

    def test_image_features_greyscale(self):
        np = self._require_numpy()
        test_image = os.path.normpath(os.path.join(DIR, "data/48by48.png"))
        response = image_features(test_image)

        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 4096)
        self.check_range(response)

    def test_image_features_rgb(self):
        np = self._require_numpy()
        test_image = os.path.normpath(os.path.join(DIR, "data/48by48rgb.png"))
        response = image_features(test_image)

        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 4096)
        self.check_range(response)

    def test_batch_image_features_greyscale(self):
        test_data = [os.path.normpath(os.path.join(DIR, "data/48by48.png"))]
        response = image_features(test_data)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(isinstance(response[0], list))
        self.assertEqual(len(response[0]), 4096)

    def test_batch_image_features_rgb(self):
        test_data = [os.path.normpath(os.path.join(DIR, "data/48by48rgb.png"))]
        response = image_features(test_data)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(isinstance(response[0], list))
        self.assertEqual(len(response[0]), 4096)

    def test_float_numpy_arrays(self):
        np = self._require_numpy()
        test_image = np.random.random(size=(48,48))
        response = image_features(test_image)

        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 4096)
        self.check_range(response)

    def test_float_RGB_numpy_arrays(self):
        np = self._require_numpy()
        test_image = np.random.random(size=(48,48,3))
        response = image_features(test_image)

        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 4096)
        self.check_range(response)

    def test_float_RGBA_numpy_arrays(self):
        np = self._require_numpy()
        test_image = np.random.random(size=(48,48,4))
        response = image_features(test_image)

        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 4096)
        self.check_range(response)

    def test_int_numpy_arrays(self):
        np = self._require_numpy()
        test_image = np.random.randint(0, 255, size=(48,48))
        response = image_features(test_image)

        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 4096)
        self.check_range(response)

    def test_int_RGB_numpy_arrays(self):
        np = self._require_numpy()
        test_image = np.random.randint(0, 255, size=(48,48, 3))
        response = image_features(test_image)

        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 4096)
        self.check_range(response)

    def test_int_RGBA_numpy_arrays(self):
        np = self._require_numpy()
        test_image = np.random.randint(0, 255, size=(48,48, 3))
        response = image_features(test_image)

        self.assertTrue(isinstance(response, list))
        self.assertEqual(len(response), 4096)
        self.check_range(response)

    def test_invalid_int_numpy_arrays(self):
        np = self._require_numpy()
        test_image = np.random.randint(255, 300, size=(48,48, 5))
        self.assertRaises(IndicoError, image_features, test_image)
