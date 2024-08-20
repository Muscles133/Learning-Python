
def main():

    greet = input("Greeting: ")
    result = value(greet)
    print (f"${value(greet)})


def value(greeting):

    if greeting.replace(" ","").lower().startswith("hello"):
        return 0
    elif greeting.replace(" ","").lower().startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()