def fibonacci(n):
    # Your code here



def fibonacci(n):
    if n == 0:
        return 0
    else:
        return n + fibonacci(n - 1)

def main():
    try:
        number = int(input("Enter a numberr : "))
        if number < 0:
            print("Please enter a non-negative integer.")
        else:
            result = fibonacci(number)
            print(f"The fibonacci of {number} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")