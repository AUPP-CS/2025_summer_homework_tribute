import unittest
from currency_conversion import currency_conversion

class TestYuanConversion(unittest.TestCase):
    def test_currency_conversion_yuan(self):
        self.assertEqual(currency_conversion('yuan', 3), 1725)

if __name__ == '__main__':
    unittest.main()
