def main():
    
    while True:
        try:
            fract = input("Fraction: ")
            percent = convert(fract)
            status = gauge(percent)
            print(status)
            break

        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
            pass



def convert(fraction):

        x,y = map(int, fraction.split("/"))

        if not isinstance(x, int):
            raise ValueError("Invalid input: Both numerator and denominator must be integers")
        if not isinstance(y, int):
            raise ValueError("Invalid input: Both numerator and denominator must be integers")
        if y > 0 and y <= x:
            raise ValueError("y must be less than x")
        if y == 0:
            raise ZeroDivisionError("y cannot be zero")
      
        percent = (x / y) * 100
        return percent
    


def gauge(p):      #p denotes percent from convert

    if p >=101:
        raise ValueError("its more than 100%")

    if p >= 99 and p <= 100:
        return("F")

    elif p <= 1:
        return("E")

    else:
        return(f"{p:.0f}%")

if __name__ == "__main__":
    main()
