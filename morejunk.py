

##def main():
 #   print("hello world")
 ##   print("this is a function")
#main()

def get_guess():
    guess = int(input("Enter a guess: "))
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("correct!")
    else:
        print("Incorrect!")



main()


