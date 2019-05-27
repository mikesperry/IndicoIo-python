import unittest

from indicoio.utils.errors import IndicoError
from indicoio.custom import Collection, collections

collection_name = "__test_python_text__"
alternate_name = "__alternate_test_python_text__"
test_data = [
    ['input 1', 'label 1'],
    ['input 11', 'label 1'],
    ['input 2', 'label 2'],
    ['input 22', 'label 2'],
    ['input 3', 'label 3'],
    ['input 33', 'label 3'],
    ['input 4', 'label 4'],
    ['input 44', 'label 4']
]

image_collection_name = "__test_python_image__"
image_test_data = [
    ["https://i.imgur.com/xUX1rvY.png", "dog"],
    ["https://i.imgur.com/xUX1rvY.png", "dog"],
    ['https://i.imgur.com/2Q0EWRz.jpg', 'cat'],
    ['https://i.imgur.com/XhUDCMP.jpg', 'cat']
]
test_user_email = 'contact@indico.io'


class CustomAPIsTestCase(unittest.TestCase):

    def setUp(self):
        try:
            Collection(collection_name).deregister()
        except IndicoError:
            pass

        try:
            Collection(alternate_name).deregister()
        except IndicoError:
            pass

        try:
            Collection(collection_name).clear()
        except IndicoError:
            pass

        try:
            Collection(image_collection_name).clear()
        except IndicoError:
            pass

        try:
            Collection(alternate_name).clear()
        except IndicoError:
            pass



    def test_add_predict(self):
        collection = Collection(collection_name)
        collection.add_data(test_data)
        collection.train()
        collection.wait()
        result = collection.predict(test_data[0][0])
        assert test_data[0][1] in result.keys()

    def test_list_collection(self):
        collection = Collection(collection_name)
        collection.add_data(test_data)
        collection.train()
        collection.wait()
        assert collections()[collection_name]

    def test_add_large_batch(self):
        collection = Collection(collection_name)
        collection.add_data(test_data*100)
        collection.train()
        collection.wait()
        result = collection.predict(test_data[0][0])
        assert test_data[0][1] in result.keys()

    def test_add_image_batch(self):
        collection = Collection(image_collection_name)
        collection.add_data(image_test_data)
        collection.train()
        collection.wait()
        result = collection.predict(image_test_data[0][0])
        assert image_test_data[0][1] in result.keys()

    def test_clear_example(self):
        collection = Collection(collection_name)
        collection.add_data(test_data)
        collection.train()
        collection.wait()
        result = collection.predict(test_data[0][0])
        assert test_data[0][1] in result.keys()
        collection.remove_example(test_data[0][0])
        collection.train()
        collection.wait()
        result = collection.predict(test_data[0][0])
        assert test_data[0][1] not in result.keys()

    def test_clear_collection(self):
        collection = Collection(collection_name)
        collection.add_data(test_data)
        collection.train()
        collection.wait()
        assert collections()[collection_name]
        collection.clear()
        assert not collections().get(collection_name)

    def test_register(self):
        collection = Collection(collection_name)
        collection.add_data(test_data)
        collection.train()
        collection.wait()
        collection.register()
        assert collection.info().get('registered')
        assert not collection.info().get('public')
        collection.deregister()
        assert not collection.info().get('registered')
        assert not collection.info().get('public')
        collection.clear()

    def test_make_public(self):
        collection = Collection(collection_name)
        collection.add_data(test_data)
        collection.train()
        collection.wait()
        collection.register(make_public=True)
        assert collection.info().get('registered')
        assert collection.info().get('public')
        collection.deregister()
        assert not collection.info().get('registered')
        assert not collection.info().get('public')
        collection.clear()

    def test_authorize_read_permissions(self):
        collection = Collection(collection_name)
        collection.add_data(test_data)
        collection.train()
        collection.wait()
        collection.register()
        collection.authorize(email=test_user_email, permission_type='read')
        assert test_user_email in collection.info().get('permissions').get('read')
        assert not test_user_email in collection.info().get('permissions').get('write')
        collection.deauthorize(email=test_user_email)
        assert not test_user_email in collection.info().get('permissions').get('read')
        assert not test_user_email in collection.info().get('permissions').get('write')
        collection.clear()

    def test_authorize_write_permissions(self):
        collection = Collection(collection_name)
        collection.add_data(test_data)
        collection.train()
        collection.wait()
        collection.register()
        collection.authorize(email=test_user_email, permission_type='write')
        assert test_user_email in collection.info().get('permissions').get('write')
        assert not test_user_email in collection.info().get('permissions').get('read')
        collection.deauthorize(email=test_user_email)
        assert not test_user_email in collection.info().get('permissions').get('read')
        assert not test_user_email in collection.info().get('permissions').get('write')
        collection.clear()

    def test_rename(self):
        collection = Collection(collection_name)
        collection.add_data(test_data)
        collection.train()
        collection.wait()
        collection.rename(alternate_name)
        new_collection = Collection(alternate_name)

        # name no longer exists
        with self.assertRaises(IndicoError):
            collection = Collection(collection_name)
            collection.train()

        # collection is now accessible via the alternate name
        new_collection.info()
        new_collection.clear()

    def test_large_add_data(self):
        collection = Collection(collection_name)
        results = collection.add_data(test_data*50, batch_size=50)
        self.assertTrue(all([result is True for result in results]))

