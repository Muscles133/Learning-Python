answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")




match answer.replace(" ","").lower():
    case "42" | "fortytwo" | "forty-two":
        print("Yes")
    case _:
        print("No")
        print("yeeeeee")