# Write a function that checks whether a given number is even or odd. 
# The function should take a single argument (the number) and 
# return "Even" if the number is even, and "Odd" if the number is odd.

def check(num):
    if num %2 == 0:
        return "even"
    elif num %2 != 0:
        return "odd"
    
def main():
    try:
        num = int(input("Give me a number and i will tell you if its odd or even: "))
        result = check(num)
        print(f"The numeber {num} is {result}")

    except ValueError:
        print("give me a proper integer")


if __name__ =="__main__":
    main()