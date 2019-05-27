from mock import patch, MagicMock
import msgpack

from indicoio.utils import is_url

mock_response = MagicMock()
mock_response.headers = {
    'x-warning': 'testing warning'
}
results = {'results': 0.5}
mock_response.status_code = 200
mock_response.json = MagicMock(return_value=results)
mock_response.content = msgpack.packb(results)

def test_is_urls():
    boring_image = [0]*(32**2)
    boring_images = [boring_image]*100

    assert not is_url(boring_image, batch=False)
    assert not is_url(boring_images, batch=True)

    url = 'http://picturepicture.com/picture'
    urls = [url]*100

    assert is_url(url, batch=False)
    assert is_url(urls, batch=True)

@patch('warnings.warn')
@patch('requests.post', MagicMock(return_value=mock_response))
def test_api_handler(mock_warn):
    from indicoio.utils.api import api_handler
    api_handler("test", cloud=None, api='sentiment')
    assert mock_warn.called_with(mock_response.headers.get('x-warning'))

@patch('warnings.warn')
@patch('requests.post', MagicMock(return_value=mock_response))
@patch('indicoio.config.host', "localhost:8000")
def test_local_host(mock_warning):
    from indicoio.utils.api import api_handler
    api_handler("test", cloud=None, api='sentiment')

