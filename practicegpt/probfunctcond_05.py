
# # Write a function that checks if a given year is a leap year. 
# # The function should take a single argument (the year) and return True if the year is a leap year, and False otherwise.

# # A year is a leap year if:

# # It is divisible by 4.
# # However, if the year is also divisible by 100, it is not a 
# # leap year unless it is also divisible by 400.

# def calculate_leap_year(year):
    
#     devide_4 = year/4
#     devide_100 = year/100
#     devide_400 = year/400

#     if devide_4.is_integer():
#         return "is a leap year"
#     elif devide_400.is_integer():
#         return "is a leap year"
#     elif devide_100.is_integer():
#         return "is not a leap year"
#     else:
#         return "is not a leap year"

# def main():
#     try:
#         year = int(input("i will tell you if they year you have supplied is a leap year: "))
#         result = calculate_leap_year(year)
#         print(f"{year} {result}")

#     except ValueError:
#         print("Provide a correct year. eg: '2012'")
        
# if __name__ == "__main__":
#     main()



def calculate_leap_year(year):
    """
    Determine if a given year is a leap year.
    
    Args:
    year (int): The year to check.
    
    Returns:
    str: "is a leap year" if the year is a leap year, "is not a leap year" otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "is a leap year"
            else:
                return "is not a leap year"
        else:
            return "is a leap year"
    else:
        return "is not a leap year"

def main():
    try:
        year = int(input("I will tell you if the year you have supplied is a leap year: "))
        result = calculate_leap_year(year)
        print(f"{year} {result}")
    except ValueError:
        print("Please provide a correct year. Example: '2012'")

if __name__ == "__main__":
    main()



