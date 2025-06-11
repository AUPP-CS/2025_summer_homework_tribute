import unittest
from currency_conversion import currency_conversion

class TestUSDConversion(unittest.TestCase):
    def test_currency_conversion_usd(self):
        self.assertEqual(currency_conversion('usd', 2), 8150)

if __name__ == '__main__':
    unittest.main()
