# Problem 4: Maximum of Three Numbers
# Write a function that takes three numbers 
# as arguments and returns the largest of the three.

def largest_number(numbers):
    
    parts = numbers.strip().split()
    
    if len(parts) != 3:
        raise ValueError("Invalid format. Please provide input in the format: 'number operator number'.")
    
    n1, n2, n3 = parts
        
    try:
        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)

    except ValueError:
        raise ValueError("Invalid numbers. Please provide valid numeric values.")

    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
    

def main():
    try:
        numbers = input("Provide me with 3 numbers formated with one space between each number and i will return the largest number: ")
        result = largest_number(numbers)
        print(f"{result} is the largest number")
    except ValueError:
        print("Incorrect format. Example: '22 44 01'")

if __name__ == "__main__":
    main()