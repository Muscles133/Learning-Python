# print("meow")

# i = 3
# while i !=0:
#     print("meow")
#     i = i-1

# i = 0
# while i <3:
#     print("meow")
#     i = i+1  # i+=1 pythonic expression


# for _ in range(3):
#     print("Meow")

#print("Meow\n"* 3, end="")  #most pythonic way. a little hard to read.

# def meow(times):
#     return "Meow" * times

# def main():

#     times = int(input("How many times do u want to meow"))
#     print("Meow\n"* times, end="")

# main()

# while True:
#     n =int(input("whats n? "))
#     if n <0:
#         break

#     for _ in range(n):
#         print("Meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Whats n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

