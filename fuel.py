def main():
    
    while True:
        try:
            fract = input("Fraction: ")
            x,y = fract.split("/")
            result = fuel_convert(x,y)
            
            if result >= 99 and result <= 100:
                print("F")
                break
            elif result <= 1:
                print("E")
                break
            elif result >=101:
                pass
            else:
                print(f"{result:.0f}%")
                break

        except (ValueError, ZeroDivisionError):
            pass



def fuel_convert(x,y):
    percent = int(x) / int(y) *100
    return percent



# def check_input(f):
#     x,y = f.split("/")






main()