def main():
    time = convert(input("What time is it? "))

    if  700 >= time < 800:
        print("Breakfast time")
    elif  1200 >= time < 1300:
        print("Lunch time")
    elif  1800 >= time < 1900:
        print("Dinner time")



def convert(t):
    if t.endwith("p.m"):
        h,m,x = t.split((":", " "))
        return h + m
    else:
        h,m = t.split(":")
        return h + m    


if __name__ == "__main__":
    main()