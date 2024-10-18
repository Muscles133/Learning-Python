#set

"""
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slythern"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = []

for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)



students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slythern"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)

    


#bank

balance = 0

def main():
    
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance: ", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n
    


if __name__ == "__main__":
    main()




class Account:
    def __int__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()
 # globals generally are not used

MEOWS = 3 # constances

for _ in range(MEOWS):
    print("meow")

    
#####

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow




#mypy to check vairables are checking the right types

def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)

  #mypy for defencencive programming

def meow(n: int):
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)




# def meow(n: int) -> str:     #below is the markdown i need for the code i am using.
#     "Meow n times.
#     :param n: Number of times to meow
#     :type n: int
#     :raise TypeError: If n is not an int
#     "return: A string of n meows, one per line
#     :rtype: str
#     """
#     return "meow\n" * n


# number: int = int(input("number: "))
# meows: str = meow(number)
# print(meows, end="")


# """


# import sys

# if len(sys.argv) == 1:
#     print("meow")

# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")

# else:
#     print("usage: meows.py")


# import argparse

# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", default=1, help="number of times to meow", type=int)
# args = parser.parse_args()

# for _ in range(int(args.n)):
#     print("meow")

#unpacking

# first, _ = input("whats your name? ").split("")
# print(f"hello, {first}")

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = [100, 50, 25]

# print(total(*coins), "knuts")


# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# coins = {"galleons": 100, "sickles": 50, "knuts":25}

# print(total(**coins), "knuts")

# def f(*args, **kwargs):
#     print("Named:", kwargs)


# f(galleons=100, sickles=50, knuts=25)

# def print(*objects, sep=" ", end="\n", ...):
#     for object in objects:
#         ...


# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())

#     print(*uppercased)


# if __name__ == "__main__":
#     main()


# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = map(str.lower, words)


#     print(*uppercased)


# if __name__ == "__main__":
#     main()


# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = [word.upper() for word in words]  # this is recreating a new list with altered words.


#     print(*uppercased)


# if __name__ == "__main__":
#     main()


# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name" : "Harry", "house": "Gryffindor"},
#     {"name" : "Ron", "house": "Gryffindor"},
#     {"name" : "Draco", "house": "Slytherin"}
# ]


# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]

# for gryffinfor in sorted(gryffindors):
#     print(gryffinfor)


# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name" : "Harry", "house": "Gryffindor"},
#     {"name" : "Ron", "house": "Gryffindor"},
#     {"name" : "Draco", "house": "Slytherin"}
# ]

# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])


# students = ["Hermione", "Harry", "Ron"]
# #gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# # for student in students:
# #     gryffindors.append({"name": student, "house": "Gryffindor", })

# print(gryffindors)



# students = ["Hermione", "Harry", "Ron"]
# gryffindors = {student: "Gryffindor" for student in students}

# print(gryffindors)


# students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i+1,students[i])

# students = ["Hermione", "Harry", "Ron"]

# for i, student in enumerate(students):
#     print(i+1, student)

###### generators!

def main():

    n = int(input("Whats n"))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("sheep" * i)
    return flock

if __name__ == "__main__":
    main()