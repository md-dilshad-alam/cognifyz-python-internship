def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").upper()


if unit == "C":
    result = celsius_to_fahrenheit(temperature)
    print("Temperature in Fahrenheit:", result)

elif unit == "F":
    result = fahrenheit_to_celsius(temperature)
    print("Temperature in Celsius:", result)

else:
    print("Invalid unit. Please enter C or F.")