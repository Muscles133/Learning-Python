
"""
def main():

    name = get_name()
    house = get_house()

    print(f"{name} from {house}")

def get_name():
    return input("What is your name? ")


def get_house():
    return input("whats your house? ")



if __name__ == "__main__":
    main()




def get_student():
    name = input("name ")
    house = input("House")
    return name, house

name, house = get_student()



stuent = get_student
print(f"{student[0]} from {student[1]}")



def main():

    student = get_student()
    #if student[0] == "Padma":
    #    student[1] = "Ravenclaw"
    print(f'{student["name"]} from {student["house"]}')

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")

    #return {"name": name, "house": house}
    


if __name__ == "__main__":
    main()


     if student["name"] == "Padma":
        student["house"] = "Ravenclaw" 




class Student:
    ...

def main():

    student = get_student()
    print(f'{student.name} from {student.house}')

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student
    


if __name__ == "__main__":
    main()




class Student:
    def __int__(self, name, house):
        self.name = name
        self.house = house

def main():

    student = get_student()
    print(f'{student.name} from {student.house}')

def get_student():
    name = input("name: ")
    house = input("house: ")
    return Student(name, house)


if __name__ == "__main__":
    main()


class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "😀"
            case _:



def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()

    """


class Student:
    def __init__(self, name, house):
        
        self.name = name
        self.house = house

       

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    

def main():
    student = get_student()
    print(student)



def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()