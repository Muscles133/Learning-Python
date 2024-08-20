def main():
    
    while True:
        try:
            fract = input("Fraction: ")
            # x,y = fract.split("/")
            # result = fuel_convert(x,y)
            print(convert(fract))
            
            # if result >= 99 and result <= 100:
            #     print("F")
            #     break
            # elif result <= 1:
            #     print("E")
            #     break
            # elif result >=101:
            #     pass
            # else:
            #     print(f"{result:.0f}%")
            #     break

        except (ValueError, ZeroDivisionError):
            pass



def convert(fraction):
    x,y = fraction.split("/")

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
    

def convert(fraction):
    ...


def gauge(percentage):
    ...





if __name__ == "__main__":
    main()


    # def check_input(f):
#     x,y = f.split("/")



