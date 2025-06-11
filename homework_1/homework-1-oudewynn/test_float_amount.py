import unittest
from currency_conversion import currency_conversion

class TestFloatAmount(unittest.TestCase):
    def test_currency_conversion_float_amount(self):
        expected_result = 2.5 * 4075
        self.assertEqual(currency_conversion('usd', 2.5), expected_result)

if __name__ == '__main__':
    unittest.main()
