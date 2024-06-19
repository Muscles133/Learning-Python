# def sum_two_numbers(a, b):
#     return int(a) + int(b)

# def main():
#     n1 = input("what is your first number ?")
#     n2 = input("what is your second number ?")
#     sum = sum_two_numbers(n1, n2)
#     print(sum)

# main()


def sum_two_numbers(a, b):
    return a + b

def main():
    try:
        n1 = float(input("What is your first number? "))
        n2 = float(input("What is your second number? "))
        result = sum_two_numbers(n1, n2)
        print(f"The sum of {n1} and {n2} is {result}.")
    except ValueError:
        print("Please enter valid numbers.")

main()
