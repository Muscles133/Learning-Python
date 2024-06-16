#ask user for their name #remove white space #capitalise return value
#ame = input ("Whats your name?").strip().title()

#split users names in first  and last
#first, last = name.split(" ")

#say hello to the user
#print(f"Hello, {first}")



def main():
    hello()
    name = input ("Whats your name? ").strip().title()
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()