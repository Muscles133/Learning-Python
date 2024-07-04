def main():
    
    while True:
        try:
            fract = input("Fraction: ")
            x,y = fract.split("/")
            result = fuel_convert(x,y)
            
            if result >= 99:
                print("F")
                break
            elif result == 0:
                print("E")
                break
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