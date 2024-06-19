# def main():
#     name = greet(input
#     print("Hello " + name + " how are you today? ")

# def greet(name):
#     return name

# main()

def greet(name):
    return "Hello " + name + " how are you today? "

def main():
    name = input("Hello what is your Name? ")
    greeting = greet(name)
    print(greeting)

main()