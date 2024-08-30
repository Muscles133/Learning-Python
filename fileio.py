import csv


"""
# names = []

# for _ in range (3):

#     #name = input("whats your name")
#     names.append(input("whats your name"))


# for name in sorted(names):
#     print(f"hello, {name}")


name = input("whats your name")

with open("names.txt", "a") as file:

    file.write (f"{name}\n")
           
#file.close()draco



with open("names.txt", "r") as file:
                                                    #     lines= file.readlines()

                                                    # for line in lines:
                                                    #     print(f"hello, {line.rstrip()}")
    for line in file:
        print("hello,", line.rstrip())



names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())


for name in sorted(names):
    print(f"hello, {name}")



# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello, ", line.rstrip())




with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")



# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.strip().split(",")
#         students.append(f"{name} is in {house}")

# for students in sorted(students):
#     print(students)

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")

"""
students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name":name, "house":home})


    # for line in file:
    #     name, house = line.strip().split(",")
    #     student ={"name": name, "house": house}
    #     students.append(student)

# def get_name(student):
#     return student["name"]

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")