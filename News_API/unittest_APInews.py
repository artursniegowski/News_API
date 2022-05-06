import unittest
import requests
from set_url import SetURL
from countries import Country_ISO_CODE

class Testunittest_APInews(unittest.TestCase):
    """testing our file python_response.py"""

    def setUp(self) -> None:
        """Create a response file and url"""
        # Creating the instance of a class
        self.url = SetURL()
        self.response_url = self.url.return_url_headlines(country=\
            Country_ISO_CODE.USA.value)
        self.response = requests.get(self.response_url)
        self.response_dict = self.response.json()

    def  test_status_code_200(self):
        """Testing that the status code from the response is 200"""    
        self.assertEqual(self.response.status_code,200)

    def test_total_results_greater_than_0(self):
        """Testing the total number of results is greater than 0"""
        self.assertGreater(self.response_dict['totalResults'],0)

unittest.main()