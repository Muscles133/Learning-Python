#aslkdfg;alsd

"""


Error Handling: Write a function that takes two numbers as input and returns their division. 
Handle the case where the second number might be zero.

Dictionaries and Lists: Create a program that stores student names and their corresponding 
grades in a dictionary. Then, calculate and print the average grade.

For Loops: Write a program that prints the first 10 even numbers using a for loop.

While Loops: Create a simple guessing game where the computer picks a random number between 1 and 10, 
and the user has to guess it. Use a while loop to keep asking for guesses until the correct number is guessed.

Conditionals: Write a program that takes a temperature in Celsius as input and prints whether it's "Cold" 
(below 10°C), "Mild" (between 10°C and 25°C), or "Hot" (above 25°C).


"""


# def main():
#     while True:
#         try:
#             no1 = int(input("First number: "))
#             no2 = int(input("Second number: "))
#             result = no1 / no2
#             print(result)
#             break

#         except:
#             print("Second value must not be '0'")
#             pass
# main()

# # def divide_numbers(a, b):
# #     try:
# #         result = a / b
# #         return result
# #     except ZeroDivisionError:
# #         return "Error: Cannot divide by zero"

# # def main():
# #     while True:
# #         try:
# #             no1 = float(input("First number: "))
# #             no2 = float(input("Second number: "))
# #             result = divide_numbers(no1, no2)
# #             print(result)
# #             break
# #         except ValueError:
# #             print("Please enter valid numbers")

# # main()
        

# numb = 20
# for i in range(2, numb+2, 2):
#     print (i)

# numb = 0
# for i in range(10):
#     numb += 2
#     print(numb)

# for i in range(20):
#     if i % 2 == 0:
#         print(i + 2)


# results = {}
# grades_d = {
   
#     "A": 90,
#     "B": 80,
#     "C": 70,
#     "D": 60,
#     "F": 50
# }

# def main():

#     while True:
#         try:
#             student = input("Students name: ")
#             grade = input("Students Grade (A,B,C,D,F): ").upper()
#             numgrade = grades_d[grade]
#             results[student] = numgrade

#         except EOFError:
#             av = 0
#             count = 0
#             for g in results:
#                 av += int(results[g])
#                 count += 1
#                 avg = av / count
#             if  avg >= 90:
#                 print("Average grade: A")
#             elif avg >= 80:
#                 print("Average grade: B")
#             elif avg >= 70:
#                 print("Average grade: C")
#             elif avg >= 60:
#                 print("Average grade: D")
#             else:
#                 print("Average grade: F")
#             break

# main()

# def get_numeric_grade(letter_grade):
#     grades = {"A": 90, "B": 80, "C": 70, "D": 60, "F": 50}
#     return grades.get(letter_grade.upper(), 0)

# def calculate_average(grades):
#     if not grades:
#         return 0
#     return sum(grades.values()) / len(grades)

# def get_letter_grade(average):
#     if average >= 90:
#         return "A"
#     elif average >= 80:
#         return "B"
#     elif average >= 70:
#         return "C"
#     elif average >= 60:
#         return "D"
#     else:
#         return "F"

# def main():
#     students = {}
#     while True:
#         name = input("Student's name (or press Enter to finish): ")
#         if name == "":
#             break
#         grade = input("Student's Grade (A,B,C,D,F): ").upper()
#         numeric_grade = get_numeric_grade(grade)
#         if numeric_grade:
#             students[name] = numeric_grade
#         else:
#             print("Invalid grade entered. Skipping this entry.")

#     average = calculate_average(students)
#     letter_grade = get_letter_grade(average)
#     print(f"Average grade: {average:.2f} ({letter_grade})")

# main()

# import random

# rand = random.randrange(1, 10)
# def main():

#     while True:
#         try:
#             guess = int(input("Guess a number from 1 to 10: "))
#             if guess == rand:
#                 print (f"You got it!! the number was {rand}")
#                 break
#             else:
#                 hint = hot_cold(guess)
#                 print(f"{hint}.....No not it try again")
        
#         except EOFError:
#             break

#         except KeyError:
#             pass

# def hot_cold(g):
#     if g < rand:
#         return "higher!"
#     else:
#         return "Lower!"
    
# main()


# import random

# def get_hint(guess, target):
#     if guess < target:
#         return "Higher!"
#     else:
#         return "Lower!"

# def play_game():
#     target = random.randint(1, 10)
#     attempts = 0
    
#     while True:
#         try:
#             guess = int(input("Guess a number from 1 to 10: "))
#             attempts += 1
            
#             if guess < 1 or guess > 10:
#                 print("Please enter a number between 1 and 10.")
#             elif guess == target:
#                 print(f"Congratulations! You guessed it in {attempts} attempts. The number was {target}.")
#                 break
#             else:
#                 hint = get_hint(guess, target)
#                 print(f"{hint} Try again.")
#         except ValueError:
#             print("Please enter a valid number.")

# play_game()


# Conditionals: Write a program that takes a temperature in Celsius as input and prints whether it's "Cold" 
# (below 10°C), "Mild" (between 10°C and 25°C), or "Hot" (above 25°C).

# def main():
#     while True: 
#         try:                                                     
#             temp = input("Provide me with celsius and i will tell you weather its hot, cold or mild: ").lower().strip()
#             s_temp = temp.replace('°', '').replace('c', '')
#             n_temp = int(s_temp)
#             if n_temp <= 9:
#                 print("it's 'Cold'")
#             elif 10 <= n_temp <= 24:
#                 print("it's 'Mild'")
#             else:
#                 print("it's 'Hot'")
        
#         except ValueError:
#             print("Please enter a input. example: '10°C' ")

# main()

# def categorize_temperature(celsius):
#     if celsius < 10:
#         return "Cold"
#     elif 10 <= celsius <= 25:
#         return "Mild"
#     else:
#         return "Hot"

# def main():
#     while True:
#         try:
#             temp_input = input("Enter a temperature in Celsius (e.g., '20' or '20°C'): ").lower().strip()
#             temp_input = temp_input.replace('°', '').replace('c', '')
#             celsius = float(temp_input)
            
#             category = categorize_temperature(celsius)
#             print(f"{celsius}°C is categorized as '{category}'")
            
#             if input("Do you want to check another temperature? (yes/no): ").lower() != 'yes':
#                 break
        
#         except ValueError:
#             print("Please enter a valid number for the temperature.")

# main()