



def fract():
    fraction = "5/7"
    xstr,ystr = fraction.split("/")
    x = int(xstr)
    y = int(ystr)

    if x is not int:
        raise ValueError
    elif y is not int:
        raise ValueError
    elif not y < x:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    else:
        percent = int(x) / int(y) *100
        return percent


fract()

print(f"{x}/{y}")