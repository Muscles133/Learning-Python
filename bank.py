Greet = input("Greeting: ")

if Greet.lower().startswith("hello"):
    print("$0")
elif Greet.lower().startswith("h"):
    print("$20")
else:
    print("$100")
