FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    celcius_temp = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius_temp


def convert_to_fahrenheit(celcius):
    fahrenheit_temp = (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit_temp


def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            result = convert_to_celcius(temp)
            print(f"{temp}°F is {result}°C")
        elif unit == 'C':
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")

        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value. ")


if __name__ == "__main__":
    main()
