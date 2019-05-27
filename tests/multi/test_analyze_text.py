from indicoio import analyze_text, IndicoError
from indicoio.text import TEXT_APIS
from .indico_multi_base import MultiTest

class AnalyzeTextTest(MultiTest):
    
    def test_multi_api_text(self):
        test_data = 'clearly an english sentence'
        response = analyze_text(test_data)

        self.assertTrue(isinstance(response, dict))
        self.assertTrue(set(response.keys()) <= set(TEXT_APIS.keys()))

    def test_batch_multi_api_text(self):
        test_data = ['clearly an english sentence']
        response = analyze_text(test_data)

        self.assertTrue(isinstance(response, dict))
        self.assertTrue(set(response.keys()) <= set(TEXT_APIS.keys()))

    def test_default_multi_api_text(self):
        test_data = 'clearly an english sentence'
        response = analyze_text(test_data)

        self.assertTrue(isinstance(response, dict))
        self.assertTrue(set(response.keys()) <= set(TEXT_APIS.keys()))

    def test_multi_api_bad_api(self):
        self.assertRaises(IndicoError,
                          analyze_text,
                          "this shouldn't work",
                          apis=["sentiment", "somethingbad"])

    def test_multi_bad_mixed_api(self):
        self.assertRaises(IndicoError,
                            analyze_text,
                            "this shouldn't work",
                            apis=["fer", "sentiment"])

    def test_batch_multi_bad_mixed_api(self):
        self.assertRaises(IndicoError,
                            analyze_text,
                        ["this shouldn't work"],
                        apis=["fer", "sentiment"])
