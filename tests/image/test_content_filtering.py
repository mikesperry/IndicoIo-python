#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from indicoio import content_filtering
from .indico_image_base import ImageTest, DIR

class ContentFilteringTest(ImageTest):

    def test_safe_content_filtering(self):
        test_face = os.path.normpath(os.path.join(DIR, "data/happy.png"))
        response = content_filtering(test_face)
        self.assertTrue(response < 0.5)

    def test_batch_content_filtering(self):
        test_data = [os.path.normpath(os.path.join(DIR, "data/48by48.png"))]
        response = content_filtering(test_data)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(isinstance(response[0], float))

    def test_resize_content_filtering(self):
        test_face = os.path.normpath(os.path.join(DIR, "data/happy.png"))
        response = content_filtering(test_face)
        self.assertTrue(isinstance(response, float))

    def test_resize_content_filtering_numpy_arrays(self):
        np = self._require_numpy()
        test_image = np.random.randint(0, 255, size=(480,248, 3))
        response = content_filtering(test_image)
        self.assertTrue(isinstance(response, float))
