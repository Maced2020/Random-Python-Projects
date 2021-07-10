#! /usr/bin/python3
# A SIMPLE PROGRAM TO CONVERT TEMP FROM F TO C OR C TO F
#started and completed on July 10 2021


def temp_converter():
    convert = input('Would you like to convert from Fahrenheit or Celsius: ').upper()
    print()
    if convert == "C" or convert == "F" or convert == "FAHRENHEIT" or convert == "CELSIUS":
        temp = input("what is the temperature now?: ")
        if convert == "C" or convert == 'CELSIUS':
            conversionc = float(temp) * 1.8 + 32
            print(conversionc)
        else:
            conversionf = (float(temp) - 32) * 0.5556
            print(conversionf)
            
    else:
        print(" you chose an invalid option try again")
        temp_converter()

temp_converter()