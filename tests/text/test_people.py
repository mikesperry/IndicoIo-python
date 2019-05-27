

from indicoio import people
from .indico_text_base import TextTest

class PeopleTest(TextTest):

    def test_people_v2(self):
        test_data = 'Barack Obama is scheduled to give a talk next Saturday at the White House.'
        response = people(test_data)
        self.assertTrue(isinstance(response, list))
        sorted_response = sorted(response, key=lambda x: x['confidence'], reverse=True)
        self.assertTrue(sorted_response[0]['text'] == 'Barack Obama')

        test_data = [test_data] * 2
        response = people(test_data)
        self.assertTrue(isinstance(response, list))
        sorted_response = [sorted(arr, key=lambda x: x['confidence'], reverse=True) for arr in response]
        self.assertEqual(len(sorted_response), 2)
        self.assertTrue(sorted_response[0][0]['text'] == 'Barack Obama')