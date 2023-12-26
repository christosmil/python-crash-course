import unittest

from city_functions import get_formatted_city

class TestCity(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_county(self):
        """Do cities like 'Santiago, Chile' work?"""
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do cities like 'Santiago, Chile - population xxx' work?"""
        formatted_city = get_formatted_city('santiago', 'chile', 
            population=5_000_000)
        expected_output = "Santiago, Chile - population 5000000"
        self.assertEqual(formatted_city, expected_output)


if __name__ == "__main__":
    unittest.main()