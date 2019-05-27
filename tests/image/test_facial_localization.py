#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from indicoio import facial_localization
from .indico_image_base import ImageTest, DIR

class FacialLocalizationTest(ImageTest):

    def test_facial_localization(self):
        test_face = os.path.normpath(os.path.join(DIR, "data/happy.png"))
        res = facial_localization(test_face)[0]
        self.assertTrue(res["top_left_corner"][0] < res["bottom_right_corner"][0])
        self.assertTrue(res["top_left_corner"][1] < res["bottom_right_corner"][1])

    def test_facial_localization_sensitivity(self):
        test_face = os.path.normpath(os.path.join(DIR, "data/happy.png"))
        low_sens = facial_localization(test_face, sensitivity=0.1)
        high_sens = facial_localization(test_face, sensitivity=0.9)
        self.assertEqual(len(low_sens), 1)
        self.assertTrue(len(high_sens) > 1)

    def test_facial_localization_crop(self):
        test_face = os.path.normpath(os.path.join(DIR, "data/happy.png"))
        res = facial_localization(test_face, crop=True)[0]
        self.assertTrue(res.get("image"))
