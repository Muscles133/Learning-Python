# Problem 1: Temperature Conversion
# Write a function that converts a temperature from Fahrenheit to Celsius. The function should take a single argument 
# (the temperature in Fahrenheit) and return the temperature in Celsius.

def temperature_coversion(temp):
    return (temp - 32) * 5/9


def main():
    try:
        temp = float(input("i will convert fahrenheit to celsius, give me the degrees: "))
        result = temperature_coversion(temp)
        print(f"{temp} in degrees fahrenheit is {result:.2f} degrees celsius")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()