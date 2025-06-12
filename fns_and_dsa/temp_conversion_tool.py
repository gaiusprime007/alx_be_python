FAHRENHEIT_TO_CELCIUS_FACTOR = 5/9
CELCIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
     celcius_temp = (fahrenheit - 32) * CELCIUS_TO_FAHRENHEIT_FACTOR
     return celcius_temp


def convert_to_fahrenheit(celcius):
     fahrenheit_temp = (celcius * CELCIUS_TO_FAHRENHEIT_FACTOR) + 32
     return fahrenheit_temp


def main():
     temp = float(input("Enter temperature to convert: "))
     unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

     if unit == 'F':
          result = convert_to_celcius(temp)
          print(f"{temp}°F is {result}°C")
     elif unit == 'C':
          result = convert_to_fahrenheit(temp)
          print(f"{temp}°C is {result}°F")

     else:
          print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
     main()
