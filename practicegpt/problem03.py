# def is_even(number):
#     if (number %2 == 0):
#         return "your number is Even"
#     else:
#         return "your number is Odd"

# def main():
#     try:
#         number = int(input("Give me a number and i will tell you if its odd or even"))
#         result = is_even(number)
#         print(result)
#     except ValueError:
#         print("Please enter valid numbers.")

# main()

def is_even(number):
    return number % 2 == 0

def main():
    try:
        number = int(input("Give me a number and I will tell you if it's odd or even: "))
        if is_even(number):
            print("Your number is Even")
        else:
            print("Your number is Odd")
    except ValueError:
        print("Please enter a valid number.")

main()
