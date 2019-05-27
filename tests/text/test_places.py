


from indicoio import places
from .indico_text_base import TextTest

class PlacesTest(TextTest):

    def test_places_v2(self):
        test_data = "Lets all go to Virginia beach before it gets too cold to wander outside."
        response = places(test_data)
        self.assertTrue(isinstance(response, list))
        sorted_response = sorted(response, key=lambda x: x['confidence'], reverse=True)
        self.assertTrue('Virginia' in sorted_response[0]['text'])

        test_data = [test_data] * 2
        response = places(test_data)
        self.assertTrue(isinstance(response, list))
        sorted_response = [sorted(arr, key=lambda x: x['confidence'], reverse=True) for arr in response]
        self.assertTrue('Virginia' in sorted_response[0][0]['text'])