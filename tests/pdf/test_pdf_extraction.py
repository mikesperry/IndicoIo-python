import os.path

import PIL
from PIL import Image
from PIL.PpmImagePlugin import PpmImageFile
import six

from indicoio import pdf_extraction
from .indico_pdf_base import PDFTestCase

DIR = os.path.dirname(os.path.realpath(__file__))
PDF = os.path.join(DIR, 'data', 'test.pdf')


class PDFExtractionTestCase(PDFTestCase):

    def test_pdf_extraction(self):
        results = pdf_extraction(PDF)
        assert 'text' in results.keys()
        assert 'metadata' in results.keys()
        assert isinstance(results.get('text'), six.string_types)
        assert isinstance(results.get('metadata'), dict)

    def test_image_support(self):
        results = pdf_extraction(PDF, images=True)
        assert 'text' in results.keys()
        assert 'metadata' in results.keys()
        assert 'images' in results.keys()
        assert isinstance(results.get('images'), list)
        assert isinstance(results.get('images')[0], PIL.JpegImagePlugin.JpegImageFile)

    def test_table_support(self):
        results = pdf_extraction(PDF, tables=True)
        assert 'text' in results.keys()
        assert 'metadata' in results.keys()
        assert 'tables' in results.keys()
        assert isinstance(results.get('tables'), list)

    def test_url_support(self):
        url = "https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf"
        results = pdf_extraction(url)
        assert 'text' in results.keys()
        assert 'metadata' in results.keys()
        assert isinstance(results.get('text'), six.string_types)
        assert isinstance(results.get('metadata'), dict)
