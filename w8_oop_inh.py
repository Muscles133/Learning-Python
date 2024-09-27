# class Wizard:
#     def __init__(self, name):
#         if not name:
#             raise ValueError("missing name")
#         self.name = name

# class Student(Wizard):
#     def __init__(self, name, house):
#         super().__init__(name)
#         self.house = house

# class Professor(Wizard):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject


# def main():


#     student = Student("Harry", "Gryffindor")
#     professor = Professor("Severus", "Defense Against teh Dark Arts")
#     wizard = Wizard("Albus")


# if __name__ == "__main__":
#     main()


# class Vault:
#     def __init__(self, galleons=0, sickles=0, knuts=0):
#         self.galleons = galleons
#         self.sickles = sickles
#         self.knuts = knuts

#     def __str__(self):
#         return f"{self.galleons} Galleons, {self.sickles}, Sickles, {self.knuts}, Knuts"

#     def __add__(self, other):
#         galleons = self.galleons + other.galleons
#         sickles = self.sickles + other.sickles
#         knuts = self.knuts + other.sickles
#         return Vault(galleons, sickles, knuts)


# potter = Vault(100, 50, 25)
# print(potter)

# weasley = Vault(25, 50, 100)
# print(weasley)

# granger = Vault(215, 501, 120)
# print(granger)

# total = weasley + potter + granger
# print(total)

# SHORT ON CLASSES


class Package:
    def __init__(self, number, sender, reciever, weight):
        self.number = number
        self.sender = sender
        self.reciever = reciever
        self.weight = weight

    def __str__(self):
        return f"Packag ID:{self.number}, Sender:{self.sender}"

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg



def main():
    # packages = {"Package1: Alice to Bob, 10kg", "Package 2: Bob to Charlie, 5kg"}

    packages = [
        Package(number=1, sender="Alice", reciever="Bob", weight=10),
        Package(number=2, sender="Bob", reciever="Alice", weight=5),
    ]

    # obj1 = Package(1, "Joe", "Alice", "10kg")

    for package in packages:
        # print(
        #     f"{package} costs: ${package.calculate_cost(cost_per_kg=2)}"
        #     )#f"Package {package.number}: {package.sender} to {package.reciever}, {package.weight}kg"

        print(f"Package {package.number}: {package.sender} to {package.reciever}, {package.weight}")

    


main()
