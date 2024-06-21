# Write a function that acts as a simple calculator. 
# The function should take three arguments: two numbers and a string representing the operation to be performed ("add", "subtract", "multiply", "divide"). 
# The function should return the result of the operation. If the operation is not one of the four specified, 
# the function should return "Invalid operation".

def calculate_numbers(cal):
    a,b,c = cal.split(" ")
    
    if b == "add" or b == "+":
        return int(a) + int (c)
    
    elif b == "subtract" or b == "-":
        return int(a) - int (c)
    
    elif b == "multiply" or b == "*":
        return int(a) * int (c)
    
    elif b == "devide" or b == "/":
        return int(a) / int (c)


def main():
    
    try:
        cal = input("I will calculate for you. The format is number operator number: ").lower()
        result = calculate_numbers(cal)
        print(f"{cal} Equeals {result}")
    
    except ValueError:
        print('Please give me the correct format ie. "5 subtract 3"')



if __name__ == "__main__":
    main()



# def calculate(expression):
#     """
#     Calculate a simple expression in the format "number operator number".
    
#     Args:
#     expression (str): The expression to calculate, e.g., "5 add 3".
    
#     Returns:
#     float: The result of the calculation.
    
#     Raises:
#     ValueError: If the input is not in the correct format or contains invalid operators.
#     ZeroDivisionError: If there is an attempt to divide by zero.
#     """
#     parts = expression.strip().split()
#     if len(parts) != 3:
#         raise ValueError("Invalid format. Please provide input in the format: 'number operator number'.")

#     a, operator, c = parts

#     try:
#         a = float(a)
#         c = float(c)
#     except ValueError:
#         raise ValueError("Invalid numbers. Please provide valid numeric values.")

#     if operator in ["add", "+"]:
#         return a + c
#     elif operator in ["subtract", "-"]:
#         return a - c
#     elif operator in ["multiply", "*"]:
#         return a * c
#     elif operator in ["divide", "/"]:
#         if c == 0:
#             raise ZeroDivisionError("Cannot divide by zero.")
#         return a / c
#     else:
#         raise ValueError("Invalid operator. Please use add (+), subtract (-), multiply (*), or divide (/).")

# def main():
#     try:
#         expression = input("I will calculate for you. The format is 'number operator number': ").lower()
#         result = calculate(expression)
#         print(f"{expression} equals {result}")
#     except ValueError as e:
#         print(e)
#     except ZeroDivisionError as e:
#         print(e)

# if __name__ == "__main__":
#     main()
