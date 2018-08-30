import unittest

from lesson3 import initcity

class CityTestCase(unittest.TestCase):

    def test_city_country(self):
        testres = initcity(" santiago ", " chile  ")
        self.assertEqual(testres,"Santiago, Chile")

    def test_city_country_population(self):
        testres = initcity(" santiago ", " chile  ",population=500000)
        self.assertEqual(testres, "Santiago, Chile - population 500000")


unittest.main()
