def convertCelsiusToKelvin(ctemp):

    float(ctemp)
    Ktemp = ctemp + 273.15
    float(Ktemp)
    return round(Ktemp, 2)


def convertCelsiusToFahrenheit(ctemp):

    float(ctemp)
    ftemp = (ctemp*9/5 + 32)
    float(ftemp)
    return round(ftemp, 2)

def convertFahrenheitToCelsius(ftemp):

    float(ftemp)
    ctemp = (ftemp-32)*5/9
    float(ctemp)
    return round(ctemp, 2)

def convertFahrenheitToKelvin(ftemp):

    float(ftemp)
    ktemp = (ftemp + 459.67)*5/9
    float(ktemp)
    return round(ktemp, 2)

def convertKelvinToFahrenheit(ktemp):

    float(ktemp)
    ftemp = (ktemp*9/5) - 459.67
    float(ftemp)
    return round(ftemp, 2)

def convertKelvinToCelsius(ktemp):

    float(ktemp)
    ctemp = ktemp - 273.15
    float(ctemp)
    return round(ctemp, 2)

def main():
    pass
if __name__ == "__main__":
    main()