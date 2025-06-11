import unittest
from currency_conversion import currency_conversion

class TestBahtConversion(unittest.TestCase):
    def test_currency_conversion_baht(self):
        self.assertEqual(currency_conversion('baht', 2), 230)

if __name__ == '__main__':
    unittest.main()
