import unittest
from currency_conversion import currency_conversion

class TestInvalidAmount(unittest.TestCase):
    def test_currency_conversion_invalid_amount(self):
        self.assertEqual(currency_conversion('usd', 'ab'), 'invalid amount')

if __name__ == '__main__':
    unittest.main()
