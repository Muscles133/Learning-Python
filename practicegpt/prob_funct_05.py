# def factorial(n):
#     if n == 0
#     return 1
#     else:
#         for n in



# def main():
#     n = int(input("Give me your factorial "))
#     result = factorial(n)




# main()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    try:
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            print("Please enter a non-negative integer.")
        else:
            result = factorial(number)
            print(f"The factorial of {number} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")

main()


