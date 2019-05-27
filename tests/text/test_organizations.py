

from indicoio import organizations
from .indico_text_base import TextTest

class OrganizationsTest(TextTest):

    def test_organizations_v2(self):
        test_data = "A year ago, the New York Times published confidential comments about ISIS ideology by Major General Michael K. Nagata, then U.S. Special Operations commander in the Middle East."
        response = organizations(test_data)
        self.assertTrue(isinstance(response, list))
        sorted_response = sorted(response, key=lambda x: x['confidence'], reverse=True)
        self.assertTrue('New York Times' in [result["text"] for result in sorted_response])

        test_data = [test_data] * 2
        response = organizations(test_data)
        self.assertTrue(isinstance(response, list))
        sorted_response = [sorted(arr, key=lambda x: x['confidence'], reverse=True) for arr in response]
        self.assertTrue('New York Times' in [result["text"] for result in sorted_response[0]])
