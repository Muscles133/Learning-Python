name = input("whats your name? ")

# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermine":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# if name == "Harry" or name == "Hermine" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Herm":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "draco":
#         print("Sly")
#     case _:
#         print("Who?")

match name:
    case "Harry" | "Ron" | "herminoe":
        print("Gryffindor")
    case "draco":
        print("Sly")
    case _:
        print("Who?")