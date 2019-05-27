import os, base64

from PIL import Image
from six import BytesIO

from indicoio.utils.preprocessing import data_preprocess
from .indico_image_base import ImageTest, DIR

class ResizeTests(ImageTest):
    """
    test image resizing
    """
    def test_min_axis_resize(self):
        test_image = os.path.normpath(os.path.join(DIR, "data/fear.png"))
        resized_image = data_preprocess(test_image, size=360, min_axis=True)
        image_string = BytesIO(base64.b64decode(resized_image))
        image = Image.open(image_string)
        self.assertEqual(image.size, (540, 360))
