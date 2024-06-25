"""
Even Number Sum:
Write a program that calculates the sum of all even numbers from 1 to 50 using a loop and a conditional.
"""



# start_value = 0
# for i in range(0, 51, 2):
#     start_value += i
# print(start_value)


# total = 0
# for i in range(2, 51, 2):
#     total += i
# print(total)


"""
Factorial Calculator:
Create a program that asks the user for a number and calculates its factorial using a loop. (Reminder: 5! = 5 * 4 * 3 * 2 * 1)
"""

# def main():
#     try:
#         number = int(input("Give me a whole number and i will give you its factorial: "))
#         if number < 0:
#             print("Please enter a non-negative integer.")
#         else:
#             result = factorial(number)
#             print(f"The Factorial of {number} is {result}")
#     except ValueError:
#         print("Please enter a valid integer.")

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         count = 1
#         for i in range(1,n+1):
#             count *= i
#         return count

# main()

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         result = 1
#         while n > 0:
#             result *= n
#             n -= 1
#         return result

"""
Prime Number Checker:
Write a program that asks the user for a number and determines if it's prime or not using a loop and conditionals.

FizzBuzz:
Implement the classic FizzBuzz problem. Print numbers from 1 to 100, but for multiples of 3 print "Fizz" 
instead of the number, for multiples of 5 print "Buzz", and for numbers that are multiples of both 3 and 5, print "FizzBuzz".

Password Strength Checker:
Create a program that asks the user for a password and checks its strength. Use loops and conditionals to ensure the password:
Is at least 8 characters long
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one digit
Contains at least one special character (e.g., !@#$%^&*)
"""

# def main():
#     prime = int(input("Give me a number and i will tell you if its a prime number: "))
#     if prime <= 1:
#         print("The number 1 is neither prime nor composite")
#     elif prime_check(prime) == True:
#         print(f"{prime} is a prime number")
#     else:
#         print(f"{prime} is not a prime number")

# def prime_check(n):
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
        
#     return True
        
# main()


# def prime_check(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True