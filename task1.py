def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def main():
    print("Temperature Converter")
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C, F, K): ").strip().upper()

    if unit == 'C':
        temp_fahrenheit = celsius_to_fahrenheit(temp)
        temp_kelvin = celsius_to_kelvin(temp)
        print(f"{temp}°C is equivalent to {temp_fahrenheit:.2f}°F and {temp_kelvin:.2f}K.")
    elif unit == 'F':
        temp_celsius = fahrenheit_to_celsius(temp)
        temp_kelvin = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F is equivalent to {temp_celsius:.2f}°C and {temp_kelvin:.2f}K.")
    elif unit == 'K':
        temp_celsius = kelvin_to_celsius(temp)
        temp_fahrenheit = kelvin_to_fahrenheit(temp)
        print(f"{temp}K is equivalent to {temp_celsius:.2f}°C and {temp_fahrenheit:.2f}°F.")
    else:
        print("Invalid unit of measurement. Please enter C, F, or K.")

if __name__ == "__main__":
    main()
