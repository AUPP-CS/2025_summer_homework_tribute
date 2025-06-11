import unittest
from currency_conversion import currency_conversion

class TestInvalidCurrency(unittest.TestCase):
    def test_currency_conversion_invalid_currency(self):
        self.assertEqual(currency_conversion('yen', 2), 'not found')

if __name__ == '__main__':
    unittest.main()
