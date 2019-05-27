#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from PIL import Image

from indicoio import fer, IndicoError
from .indico_image_base import ImageTest, DIR

class FERTest(ImageTest):

    def test_happy_fer(self):
        test_face = os.path.normpath(os.path.join(DIR, "data/happy.png"))
        response = fer(test_face)
        self.assertTrue(isinstance(response, dict))
        self.assertTrue(response['Happy'] > 0.5)

    def test_happy_fer_pil(self):
        test_face = Image.open(os.path.normpath(os.path.join(DIR, "data/happy.png"))).convert('L');
        response = fer(test_face)
        self.assertTrue(isinstance(response, dict))
        self.assertTrue(response['Happy'] > 0.5)

    def test_fear_fer(self):
        test_face = os.path.normpath(os.path.join(DIR, "data/fear.png"))
        response = fer(test_face)
        self.assertTrue(isinstance(response, dict))
        self.assertTrue(response['Fear'] > 0.25)

    def test_bad_fer(self):
        fer_set = set(['Angry', 'Sad', 'Neutral', 'Surprise', 'Fear', 'Happy'])
        test_face = os.path.normpath(os.path.join(DIR, "data/64by64.png"))
        response = fer(test_face)

        self.assertTrue(isinstance(response, dict))
        self.assertEqual(fer_set, set(response.keys()))

    def test_int_array_fer(self):
        fer_set = set(['Angry', 'Sad', 'Neutral', 'Surprise', 'Fear', 'Happy'])
        test_face = os.path.normpath(os.path.join(DIR, "data/48by48.png"))
        response = fer(test_face)

        self.assertTrue(isinstance(response, dict))
        self.assertEqual(fer_set, set(response.keys()))

    def test_batch_fer(self):
        test_data = [os.path.normpath(os.path.join(DIR, "data/48by48.png"))]
        response = fer(test_data)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(isinstance(response[0], dict))

    def test_batch_fer_bad_b64(self):
        test_data = ["$bad#FI jeaf9(#0"]
        self.assertRaises(IndicoError, fer, test_data)

    def test_batch_fer_good_b64(self):
        test_data = ["iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAg5JREFUeNrEV4uNgzAMpegGyAgZgQ3KBscIjMAGx03QEdqbgG5AOwG3AWwAnSCXqLZkuUkwhfYsvaLm5xc7sZ1dIhdtUVjsLZRFTvp+LSaLq8UZ/s+KMSbZCcY5RV9E4QQKHG7QtgeCGv4PFt8WpzkCcztu3TiL0eJgkQmsVFn0MK+LzYkRKEGpG1GDyZdKRdaolhAoJewXnJsO1jtKCFDlChZAFxyJj2PnBRU20KZg7oMlOAENijpi8hwmGkKkZW2GzONtVLA/DxHAhTO2I7MCVBSQ6nGDlEBJDhyVYiUBHXBxzQm0wE4FzPYsGs856dA9SAAP2oENzFYqR6iAFQpHIAUzO/nxnOgthF/lM3w/3U8KYXTwxG/1IgIulF+wPQUXDMl75UoJZIHstRWpaGb8IGYqwBoKlG/lgpzoUEBoj50p8QtVrmHgaaXyC/H3BFC+e9kGFlCB0CtBF7FifQ8D9zjQQHj0pdOM3F1pUBoFKdxtqkMClScHJCSDlSxhHSNRT5K+FaZnHglrz+AGoxZLKNLYH6s3CkkuyJlp58wviZ4PuSCWDXl5hmjZtxcSCGbDUD3gK7EMOZBLCETrgVBF5K0lI5bIZ0wfrYh8NWHIAiNTPHpuTOKpCes1VTFaiNaFdGwPfdmaqlj6LmjJbgoSSfUW74K3voz+/W0oIeB7HWu2s+dfx3N+eLX8CTAAwUmKjK/dHS4AAAAASUVORK5CYII="]
        response = fer(test_data)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(isinstance(response[0], dict))

    def test_batch_fer_filepath(self):
        test_data = [os.path.normpath(os.path.join(DIR, "data/fear.png"))]
        response = fer(test_data, sensitivity=.95)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(isinstance(response[0], dict))

    def test_fer_detect(self):
        test_data = os.path.normpath(os.path.join(DIR, "data/fear.png"))
        response = fer(test_data, detect=True, sensitivity=.2)
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 1)
        self.assertIn("location", response[0])

    def test_batch_fer_pil_image(self):
        test_data = [Image.open(os.path.normpath(os.path.join(DIR, "data/fear.png")))]
        response = fer(test_data)
        self.assertTrue(isinstance(response, list))
        self.assertTrue(isinstance(response[0], dict))

    def test_batch_fer_nonexistant_filepath(self):
        test_data = ["data/unhappy.png"]
        self.assertRaises(IndicoError, fer, test_data)
