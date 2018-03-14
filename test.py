import unittest
import conversions


class ConversionsTesting(unittest.TestCase):
    CTOKVALUES = ((-89.2, 183.95),
                  (-17.78, 255.37),
                  (0, 273.15),
                  (15, 288.15),
                  (37, 310.15))

    def testCTOK(self):

        print 'tests that convertCelsiusToKelvin returns the values that are correct'
        for integer, numeral in self.CTOKVALUES:
            result = conversions.convertCelsiusToKelvin(integer)
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

    CTOFVALUES = ((50, 122),
                  (40, 104),
                  (0, 32),
                  (-10, 14),
                  (30, 86))

    def testCTOF(self):

        print 'tests that convertCelsiusToFahrenheit returns the values that are correct'
        for integer, numeral in self.CTOFVALUES:
            result = conversions.convertCelsiusToFahrenheit(integer)
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

    FTOCVALUES = ((932, 500),
                  (68, 20),
                  (32, 0),
                  (50, 10),
                  (14, -10))

    def testFTOC(self):

        print 'tests that convertFahrenheitToCelcius returns the values that are correct'
        for integer, numeral in self.FTOCVALUES:
            result = conversions.convertFahrenheitToCelsius(integer)
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

    FTOKVALUES = ((932, 773.15),
                  (158, 343.15),
                  (32, 273.15),
                  (-4, 253.15),
                  (14, 263.15))

    def testFTOK(self):

        print 'tests that convertFahrenheitToKelvin returns the values that are correct'
        for integer, numeral in self.FTOKVALUES:
            result = conversions.convertFahrenheitToKelvin(integer)
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

    ktofvalues = ((773.15, 932),
                  (343.15, 158),
                  (273.15, 32),
                  (253.15, -4),
                  (263.15, 14))

    def testKtoF(self):

        print 'tests that convertKelvinToFahrenheit returns the values that are correct'
        for integer, numeral in self.ktofvalues:
            result = conversions.convertKelvinToFahrenheit(integer)
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')

    ktocvalues = ((773.15, 500),
                  (343.15, 70),
                  (273.15, 0),
                  (253.15, -20),
                  (263.15, -10))

    def testKtoC(self):

        print 'tests that convertKelvinToCelsius returns the values that are correct'
        for integer, numeral in self.ktocvalues:
            result = conversions.convertKelvinToCelsius(integer)
            self.assertEqual(numeral, result, msg='Incorrect result, calculation error')


if __name__ == "__main__":
    unittest.main()