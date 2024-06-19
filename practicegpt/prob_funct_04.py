# def find_largest(a, b, c):
#     if a < b or c:
#         return a
#     elif b < a or c:
#         return b
#     else:
#         return c


# def main():
#     try:
#         numbers = input("give me 3 numbers ")
#         a,b,c = numbers.split(" ")

#         print(a)
#         print(b)
#         print(c)

#         result = find_largest(a, b, c)
#         print( result + " is the largest number")

#     except ValueError:
#         print("Please enter a valid number.")



# main()

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def main():
    try:
        numbers = input("Give me 3 numbers separated by spaces: ")
        a, b, c = map(float, numbers.split())

        result = find_largest(a, b, c)
        print(f"{result} is the largest number")

    except ValueError:
        print("Please enter valid numbers.")

main()
