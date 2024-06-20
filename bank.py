Greet = input("Greeting: ")

if Greet.replace(" ","").lower().startswith("hello"):
    print("$0")
elif Greet.replace(" ","").lower().startswith("h"):
    print("$20")
else:
    print("$100")

#testicle