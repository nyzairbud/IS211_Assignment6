import conversions_refactored
import unittest
import random


class KnownTemperatureValues(unittest.TestCase):
    knownTemperatureValues = ((0.0, 273.15, 32.0),
                              (300.0, 573.15, 572.0),
                              (25.49, 298.64, 77.882),
                              (200, 473.15, 392),
                              (150.00, 423.15, 302.00),
                              (-220.00, 53.15, -364.00),
                              (-40.0, 233.15, -40.0),
                              )

    def testConvert(self):
        print "\nNow testing convert() function with temperature:"

        for i in range(0, len(self.knownTemperatureValues)):
            print "   TESTING ROUND %i" % (i + 1)

            CtoK = conversions_refactored.convert("Celcius", "Kelvin", self.knownTemperatureValues[i][0])
            self.assertAlmostEqual(CtoK, self.knownTemperatureValues[i][1], 4)
            print "      Checking %f celcius is converted to %f kelvin; actual: %f" % (
            self.knownTemperatureValues[i][0], self.knownTemperatureValues[i][1], CtoK)

            CtoF = conversions_refactored.convert("Celcius", "Fahrenheit", self.knownTemperatureValues[i][0])
            self.assertAlmostEqual(CtoF, self.knownTemperatureValues[i][2], 4)
            print "      Checking %f celcius is converted to %f fahrenheit; actual: %f" % (
            self.knownTemperatureValues[i][0], self.knownTemperatureValues[i][2], CtoF)

            KtoC = conversions_refactored.convert("Kelvin", "Celcius", self.knownTemperatureValues[i][1])
            self.assertAlmostEqual(KtoC, self.knownTemperatureValues[i][0], 4)
            print "      Checking %f kelvin is converted to %f celcius; actual: %f" % (
            self.knownTemperatureValues[i][1], self.knownTemperatureValues[i][0], KtoC)

            KtoF = conversions_refactored.convert("Kelvin", "Fahrenheit", self.knownTemperatureValues[i][1])
            self.assertAlmostEqual(KtoF, self.knownTemperatureValues[i][2], 4)
            print "      Checking %f kelvin is converted to %f fahrenheit; actual: %f" % (
            self.knownTemperatureValues[i][1], self.knownTemperatureValues[i][2], KtoF)

            FtoC = conversions_refactored.convert("Fahrenheit", "Celcius", self.knownTemperatureValues[i][2])
            self.assertAlmostEqual(FtoC, self.knownTemperatureValues[i][0], 4)
            print "      Checking %f fahrenheit is converted to %f celcius; actual: %f" % (
            self.knownTemperatureValues[i][2], self.knownTemperatureValues[i][0], FtoC)

            FtoK = conversions_refactored.convert("Fahrenheit", "Kelvin", self.knownTemperatureValues[i][2])
            self.assertAlmostEqual(FtoK, self.knownTemperatureValues[i][1], 4)
            print "      Checking %f fahrenheit is converted to %f kelvin; actual: %f" % (
            self.knownTemperatureValues[i][2], self.knownTemperatureValues[i][1], FtoK)
            print ""


class DistanceValues(unittest.TestCase):
    DistanceValues = ((0, 0, 0),
                           (1, 1760, 1609.344),
                           (15, 26400, 24140.16),
                           (0.0006213712, 1.0936133, 1),
                           (0.0005682, 1, 0.91440))

    def testConvert(self):
        print "\nNow testing convert() function with distance:"

        for i in range(0, len(self.DistanceValues)):
            print "   TESTING ROUND %i" % (i + 1)

            MtoY = conversions_refactored.convert("Miles", "Yards", self.DistanceValues[i][0])
            self.assertAlmostEqual(MtoY, self.DistanceValues[i][1], 4)
            print "      Checking %f miles is converted to %f yards; actual: %f" % (
            self.DistanceValues[i][0], self.DistanceValues[i][1], MtoY)

            MtoM = conversions_refactored.convert("Miles", "Meters", self.DistanceValues[i][0])
            self.assertAlmostEqual(MtoM, self.DistanceValues[i][2], 4)
            print "      Checking %f miles is converted to %f meters; actual: %f" % (
            self.DistanceValues[i][0], self.DistanceValues[i][2], MtoM)

            YtoM = conversions_refactored.convert("Yards", "Miles", self.DistanceValues[i][1])
            self.assertAlmostEqual(YtoM, self.DistanceValues[i][0], 4)
            print "      Checking %f yards is converted to %f miles; actual: %f" % (
            self.DistanceValues[i][1], self.DistanceValues[i][0], YtoM)

            YtoMe = conversions_refactored.convert("Yards", "Meters", self.DistanceValues[i][1])
            self.assertAlmostEqual(YtoMe, self.DistanceValues[i][2], 4)
            print "      Checking %f yards is converted to %f meters; actual: %f" % (
            self.DistanceValues[i][1], self.DistanceValues[i][2], YtoMe)

            MetoM = conversions_refactored.convert("Meters", "Miles", self.DistanceValues[i][2])
            self.assertAlmostEqual(MetoM, self.DistanceValues[i][0], 4)
            print "      Checking %f meters is converted to %f miles; actual: %f" % (
            self.DistanceValues[i][2], self.DistanceValues[i][0], MetoM)

            MetoY = conversions_refactored.convert("Meters", "Yards", self.DistanceValues[i][2])
            self.assertAlmostEqual(MetoY, self.DistanceValues[i][1], 4)
            print "      Checking %f meters is converted to %f yards; actual: %f" % (
            self.DistanceValues[i][2], self.DistanceValues[i][1], MetoY)
            print ""


class SanityCheck(unittest.TestCase):
    def testSanity(self):
        print "\nNow testing sanity of convert():"
        for i in range(0, 5):
            print "   TESTING ROUND %i" % (i + 1)

            celciusInput = random.random() * 100
            celciusConverted = conversions_refactored.convert("Celcius", "Celcius", celciusInput)
            self.assertAlmostEqual(celciusInput, celciusConverted, 4)
            print "      %f Celcius converted to Celcius is %f" % (celciusInput, celciusConverted)

            kelvinInput = random.random() * 1000
            kelvinConverted = conversions_refactored.convert("Kelvin", "Kelvin", kelvinInput)
            self.assertAlmostEqual(kelvinInput, kelvinConverted, 4)
            print "      %f Kelvin converted to Kelvin is %f" % (kelvinInput, kelvinConverted)

            fahrenheitInput = random.random() * 100
            fahrenheitConverted = conversions_refactored.convert("Fahrenheit", "Fahrenheit", fahrenheitInput)
            self.assertAlmostEqual(fahrenheitInput, fahrenheitConverted, 4)
            print "      %f Fahrenheit converted to Fahrenheit is %f" % (fahrenheitInput, fahrenheitConverted)

            metersInput = random.random() * 100
            metersConverted = conversions_refactored.convert("Meters", "Meters", metersInput)
            self.assertAlmostEqual(metersInput, metersConverted, 4)
            print "      %f Meters converted to Meters is %f" % (metersInput, metersConverted)

            yardsInput = random.random() * 100
            yardsConverted = conversions_refactored.convert("Yards", "Yards", yardsInput)
            self.assertAlmostEqual(yardsInput, yardsConverted, 4)
            print "      %f Yards converted to Yards is %f" % (yardsInput, yardsConverted)

            milesInput = random.random() * 100
            milesConverted = conversions_refactored.convert("Miles", "Miles", milesInput)
            self.assertAlmostEqual(milesInput, milesConverted, 4)
            print "      %f Miles converted to Miles is %f" % (milesInput, milesConverted)
            print ""


class IncompatibleUnits(unittest.TestCase):
    def testIncompatibleUnits(self):
        print "\nNow testing all incompatible units raises ConversionNotPossibleException:"

        print "   Checking if Miles-Celcius raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Miles", "Celcius", 0)

        print "   Checking if Miles-Kelvin raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Miles", "Kelvin", 0)

        print "   Checking if Miles-Fahrenheit raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Miles", "Fahrenheit", 0)

        print "   Checking if Yards-Celcius raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Yards", "Celcius", 0)

        print "   Checking if Yards-Kelvin raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Yards", "Kelvin", 0)

        print "   Checking if Yards-Fahrenheit raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Yards", "Fahrenheit", 0)

        print "   Checking if Meters-Celcius raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Meters", "Celcius", 0)

        print "   Checking if Meters-Kelvin raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Meters", "Kelvin", 0)

        print "   Checking if Meters-Fahrenheit raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Meters", "Fahrenheit", 0)

        print "   Checking if Celcius-Miles raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Celcius", "Miles", 0)

        print "   Checking if Celcius-Yards raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Celcius", "Yards", 0)

        print "   Checking if Celcius-Meters raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Celcius", "Meters", 0)

        print "   Checking if Kelvin-Miles raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Kelvin", "Miles", 0)

        print "   Checking if Kelvin-Yards raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Kelvin", "Yards", 0)

        print "   Checking if Kelvin-Meters raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Kelvin", "Meters", 0)

        print "   Checking if Fahrenheit-Miles raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Fahrenheit", "Miles", 0)

        print "   Checking if Fehrenheit-Yards raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Fahrenheit", "Yards", 0)

        print "   Checking if Fehrenheit-Meters raises ConversionNotPossibleException"
        self.assertRaises(conversions_refactored.ConversionNotPossibleException, conversions_refactored.convert,
                          "Fahrenheit", "Meters", 0)


if __name__ == "__main__":
    unittest.main()